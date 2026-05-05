import asyncio
import json
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    WebAppInfo,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

# ========== КОНФИГУРАЦИЯ ==========
TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_БОТА")
ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_IDS", "123456789").split(",")]
PORT = int(os.getenv("PORT", 8080))
RENDER_URL = os.getenv("RENDER_URL", "https://your-app.onrender.com")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ========== БАЗА ДАННЫХ ==========
DATA_FILE = "store_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "payment_details": {
            "bank": {
                "bank_name": "SBERBANK",
                "recipient": "ИП Иванов И.И.",
                "inn": "770000000000",
                "account": "40802810000000000000",
                "bik": "044525225"
            },
            "crypto": {
                "TON": "UQD...ваш_адрес_ton",
                "USDT": "TJ...ваш_адрес_usdt"
            }
        },
        "orders": []
    }

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ========== СОСТОЯНИЯ ==========
class AdminStates(StatesGroup):
    waiting_bank_name = State()
    waiting_recipient = State()
    waiting_inn = State()
    waiting_account = State()
    waiting_bik = State()
    waiting_ton = State()
    waiting_usdt = State()

# ========== КЛАВИАТУРЫ ==========
def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🛍 ОТКРЫТЬ МАГАЗИН", web_app=WebAppInfo(url=f"{RENDER_URL}/ssss.html"))]],
        resize_keyboard=True
    )

def admin_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏦 Изменить банк", callback_data="admin_bank")],
        [InlineKeyboardButton(text="💎 Изменить крипту", callback_data="admin_crypto")],
        [InlineKeyboardButton(text="📋 Заказы", callback_data="admin_orders")],
        [InlineKeyboardButton(text="🛍 Магазин", web_app=WebAppInfo(url=f"{RENDER_URL}/ssss.html"))]
    ])

# ========== КОМАНДЫ ==========
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id in ADMIN_IDS:
        await message.answer("🎨 *NEON MARKETPLACE - АДМИНКА*", parse_mode="Markdown", reply_markup=admin_keyboard())
    else:
        await message.answer("🔥 *NEON MARKETPLACE*\n\nДобро пожаловать!", parse_mode="Markdown", reply_markup=main_keyboard())

# ========== АДМИНКА ==========
@dp.callback_query(F.data == "admin_bank")
async def admin_bank(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_IDS: return
    await callback.message.answer("Введите название банка:")
    await state.set_state(AdminStates.waiting_bank_name)

@dp.message(AdminStates.waiting_bank_name)
async def p1(message: types.Message, state: FSMContext):
    await state.update_data(bank_name=message.text)
    await message.answer("Получатель:")
    await state.set_state(AdminStates.waiting_recipient)

@dp.message(AdminStates.waiting_recipient)
async def p2(message: types.Message, state: FSMContext):
    await state.update_data(recipient=message.text)
    await message.answer("ИНН:")
    await state.set_state(AdminStates.waiting_inn)

@dp.message(AdminStates.waiting_inn)
async def p3(message: types.Message, state: FSMContext):
    await state.update_data(inn=message.text)
    await message.answer("Счёт:")
    await state.set_state(AdminStates.waiting_account)

@dp.message(AdminStates.waiting_account)
async def p4(message: types.Message, state: FSMContext):
    await state.update_data(account=message.text)
    await message.answer("БИК:")
    await state.set_state(AdminStates.waiting_bik)

@dp.message(AdminStates.waiting_bik)
async def p5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    store = load_data()
    store["payment_details"]["bank"] = {
        "bank_name": data["bank_name"], "recipient": data["recipient"],
        "inn": data["inn"], "account": data["account"], "bik": message.text
    }
    save_data(store)
    await message.answer("✅ Банк обновлён!")
    await state.clear()

@dp.callback_query(F.data == "admin_crypto")
async def admin_crypto(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_IDS: return
    await callback.message.answer("TON адрес:")
    await state.set_state(AdminStates.waiting_ton)

@dp.message(AdminStates.waiting_ton)
async def c1(message: types.Message, state: FSMContext):
    await state.update_data(ton=message.text)
    await message.answer("USDT (TRC-20):")
    await state.set_state(AdminStates.waiting_usdt)

@dp.message(AdminStates.waiting_usdt)
async def c2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    store = load_data()
    store["payment_details"]["crypto"] = {"TON": data["ton"], "USDT": message.text}
    save_data(store)
    await message.answer("✅ Крипта обновлена!")
    await state.clear()

@dp.callback_query(F.data == "admin_orders")
async def admin_orders(callback: types.CallbackQuery):
    if callback.from_user.id not in ADMIN_IDS: return
    store = load_data()
    if not store["orders"]:
        await callback.message.answer("Нет заказов")
        return
    text = "📋 *ЗАКАЗЫ:*\n\n"
    for o in store["orders"][-10:]:
        text += f"#{o['id']} | {o['date']}\n{o['product']} | {o['size']} | {o['price']}₽\n{o['shop']}\n\n"
    await callback.message.answer(text, parse_mode="Markdown")

# ========== API ==========
async def handle_payment(request):
    return web.json_response(load_data()["payment_details"])

async def handle_order(request):
    try:
        data = await request.json()
        store = load_data()
        order = {
            "id": len(store["orders"]) + 1,
            "user": data.get("user", "anon"),
            "user_id": data.get("user_id"),
            "product": data.get("product"),
            "size": data.get("size"),
            "price": data.get("price"),
            "shop": data.get("shop"),
            "country": data.get("country"),
            "city": data.get("city"),
            "payment_method": data.get("payment_method"),
            "date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        store["orders"].append(order)
        save_data(store)
        
        for aid in ADMIN_IDS:
            try:
                await bot.send_message(aid, f"🛍 Заказ #{order['id']}\n{order['product']} | {order['price']}₽")
            except: pass
        
        return web.json_response({"status": "ok", "order_id": order["id"]})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=400)

async def handle_html(request):
    return web.FileResponse("ssss.html")

# ========== ЗАПУСК ==========
app = web.Application()
app.router.add_get("/api/payment-details", handle_payment)
app.router.add_post("/api/order", handle_order)
app.router.add_get("/ssss.html", handle_html)
app.router.add_get("/", handle_html)

async def main():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"🤖 Бот на порту {PORT}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
