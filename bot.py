import asyncio
import json
import os
from datetime import datetime
from aiohttp import web

# ========== КОНФИГУРАЦИЯ ==========
TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_IDS = [int(id.strip()) for id in os.getenv("ADMIN_IDS", "0").split(",") if id.strip()]
PORT = int(os.getenv("PORT", "8080"))
RENDER_URL = os.getenv("RENDER_URL", "")
TG_API = f"https://api.telegram.org/bot{TOKEN}"

# ========== ХРАНИЛИЩЕ ==========
DATA_FILE = "store_data.json"

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        data = {
            "payment_details": {
                "bank": {
                    "bank_name": "SBERBANK",
                    "recipient": "ИП Иванов И.И.",
                    "inn": "770000000000",
                    "account": "40802810000000000000",
                    "bik": "044525225"
                },
                "crypto": {
                    "TON": "UQD...",
                    "USDT": "TJ..."
                }
            },
            "orders": [],
            "admin_state": {}
        }
        save_data(data)
        return data

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ========== TELEGRAM ОТПРАВКА ==========
async def send_message(chat_id, text, reply_markup=None):
    import aiohttp
    url = f"{TG_API}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if reply_markup:
        data["reply_markup"] = json.dumps(reply_markup)
    
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=data)

# ========== КЛАВИАТУРЫ ==========
def admin_menu():
    return {
        "inline_keyboard": [
            [{"text": "🏦 Банк", "callback_data": "bank"}, {"text": "💎 Крипта", "callback_data": "crypto"}],
            [{"text": "📋 Заказы", "callback_data": "orders"}],
            [{"text": "🛍 Открыть магазин", "web_app": {"url": f"{RENDER_URL}/ssss.html"}}]
        ]
    }

def main_menu():
    return {
        "keyboard": [[{"text": "🛍 ОТКРЫТЬ МАГАЗИН", "web_app": {"url": f"{RENDER_URL}/ssss.html"}}]],
        "resize_keyboard": True
    }

# ========== WEBHOOK ОБРАБОТЧИК ==========
async def webhook(request):
    try:
        update = await request.json()
        
        if "message" in update:
            msg = update["message"]
            chat_id = msg["chat"]["id"]
            text = msg.get("text", "")
            
            # /start
            if text == "/start":
                if chat_id in ADMIN_IDS:
                    await send_message(chat_id, "🎨 <b>NEON MARKETPLACE</b>\nАдмин-панель:", admin_menu())
                else:
                    await send_message(chat_id, "🔥 <b>NEON MARKETPLACE</b>\nДобро пожаловать!", main_menu())
            
            # Обработка состояний админки
            else:
                store = load_data()
                state = store["admin_state"].get(str(chat_id))
                
                if state:
                    if state == "waiting_bank_name":
                        store["admin_state"][str(chat_id)] = {"state": "waiting_recipient", "bank_name": text}
                        save_data(store)
                        await send_message(chat_id, "Введите получателя:")
                    
                    elif state["state"] == "waiting_recipient":
                        store["admin_state"][str(chat_id)] = {
                            "state": "waiting_inn",
                            "bank_name": state["bank_name"],
                            "recipient": text
                        }
                        save_data(store)
                        await send_message(chat_id, "Введите ИНН:")
                    
                    elif state["state"] == "waiting_inn":
                        store["admin_state"][str(chat_id)] = {
                            "state": "waiting_account",
                            "bank_name": state["bank_name"],
                            "recipient": state["recipient"],
                            "inn": text
                        }
                        save_data(store)
                        await send_message(chat_id, "Введите счёт:")
                    
                    elif state["state"] == "waiting_account":
                        store["admin_state"][str(chat_id)] = {
                            "state": "waiting_bik",
                            "bank_name": state["bank_name"],
                            "recipient": state["recipient"],
                            "inn": state["inn"],
                            "account": text
                        }
                        save_data(store)
                        await send_message(chat_id, "Введите БИК:")
                    
                    elif state["state"] == "waiting_bik":
                        store["payment_details"]["bank"] = {
                            "bank_name": state["bank_name"],
                            "recipient": state["recipient"],
                            "inn": state["inn"],
                            "account": state["account"],
                            "bik": text
                        }
                        del store["admin_state"][str(chat_id)]
                        save_data(store)
                        await send_message(chat_id, "✅ Банковские реквизиты обновлены!")
                    
                    elif state == "waiting_ton":
                        store["admin_state"][str(chat_id)] = {"state": "waiting_usdt", "ton": text}
                        save_data(store)
                        await send_message(chat_id, "Введите USDT адрес:")
                    
                    elif state["state"] == "waiting_usdt":
                        store["payment_details"]["crypto"] = {
                            "TON": state["ton"],
                            "USDT": text
                        }
                        del store["admin_state"][str(chat_id)]
                        save_data(store)
                        await send_message(chat_id, "✅ Крипто-реквизиты обновлены!")
        
        # Callback от кнопок
        elif "callback_query" in update:
            cb = update["callback_query"]
            chat_id = cb["message"]["chat"]["id"]
            data = cb["data"]
            
            if chat_id in ADMIN_IDS:
                if data == "bank":
                    store = load_data()
                    store["admin_state"][str(chat_id)] = "waiting_bank_name"
                    save_data(store)
                    await send_message(chat_id, "Введите название банка:")
                
                elif data == "crypto":
                    store = load_data()
                    store["admin_state"][str(chat_id)] = "waiting_ton"
                    save_data(store)
                    await send_message(chat_id, "Введите TON адрес:")
                
                elif data == "orders":
                    store = load_data()
                    if not store["orders"]:
                        await send_message(chat_id, "📋 Заказов пока нет")
                    else:
                        text = "<b>📋 ПОСЛЕДНИЕ ЗАКАЗЫ:</b>\n\n"
                        for o in store["orders"][-10:]:
                            text += f"#{o['id']} | {o['date']}\n{o['product']} | {o['price']}₽\n{o['shop']}\n\n"
                        await send_message(chat_id, text)
        
        return web.Response(text="ok")
    except Exception as e:
        print(f"Error: {e}")
        return web.Response(text="ok")

# ========== API ==========
async def api_payment(request):
    return web.json_response(load_data()["payment_details"])

async def api_order(request):
    try:
        data = await request.json()
        store = load_data()
        order = {
            "id": len(store["orders"]) + 1,
            "user": data.get("user", "anon"),
            "product": data.get("product"),
            "size": data.get("size"),
            "price": data.get("price"),
            "shop": data.get("shop"),
            "country": data.get("country"),
            "city": data.get("city"),
            "date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        store["orders"].append(order)
        save_data(store)
        
        # Уведомление админам
        for aid in ADMIN_IDS:
            await send_message(aid, f"🛍 <b>Новый заказ #{order['id']}</b>\n{order['product']} | {order['price']}₽\n{order['shop']}")
        
        return web.json_response({"status": "ok"})
    except:
        return web.json_response({"status": "error"}, status=400)

async def index(request):
    return web.FileResponse("ssss.html")

# ========== УСТАНОВКА WEBHOOK ==========
async def set_webhook():
    import aiohttp
    url = f"{TG_API}/setWebhook?url={RENDER_URL}/webhook"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(await resp.text())

# ========== ЗАПУСК ==========
app = web.Application()
app.router.add_post("/webhook", webhook)
app.router.add_get("/api/payment-details", api_payment)
app.router.add_post("/api/order", api_order)
app.router.add_get("/ssss.html", index)
app.router.add_get("/", index)

async def main():
    await set_webhook()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"✅ Бот на порту {PORT}")

if __name__ == "__main__":
    asyncio.run(main())
