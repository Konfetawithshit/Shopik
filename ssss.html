<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>NEON STREET WEAR | Cyberpunk Store</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Courier New', monospace;
            background: #0a0010;
            color: #b44dff;
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 30% 20%, rgba(180, 77, 255, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 70% 60%, rgba(200, 0, 255, 0.1) 0%, transparent 50%);
        }

        .scanlines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px);
            pointer-events: none;
            z-index: 1000;
        }

        .page {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            min-height: 100vh;
            display: none;
            flex-direction: column;
            position: relative;
        }

        .page.active {
            display: flex;
            animation: glitchIn 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        @keyframes glitchIn {
            0% { opacity: 0; transform: translateX(-10px); filter: hue-rotate(90deg); }
            20% { transform: translateX(10px); filter: hue-rotate(-90deg); }
            100% { opacity: 1; transform: translateX(0); filter: hue-rotate(0); }
        }

        .neon-text {
            font-size: 32px;
            font-weight: bold;
            color: #b44dff;
            text-shadow: 0 0 10px #b44dff, 0 0 20px #b44dff, 0 0 40px #b44dff;
            letter-spacing: 4px;
            text-transform: uppercase;
        }

        .cyber-card {
            background: linear-gradient(135deg, rgba(20,0,40,0.95), rgba(40,0,80,0.9));
            border: 1px solid #b44dff;
            border-radius: 8px;
            padding: 20px;
            cursor: pointer;
            backdrop-filter: blur(10px);
            margin: 10px 0;
            transition: all 0.3s ease;
        }

        .cyber-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 20px rgba(180,77,255,0.3);
        }

        .cyber-btn {
            background: linear-gradient(45deg, #1a0030, #2a0050);
            border: 2px solid #b44dff;
            color: #b44dff;
            padding: 15px 30px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            text-transform: uppercase;
            cursor: pointer;
            width: 100%;
            margin: 10px 0;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        .cyber-btn:hover {
            background: linear-gradient(45deg, #b44dff, #c800ff);
            color: #0a0010;
            transform: scale(1.02);
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin: 20px 0;
        }

        .product-card {
            background: rgba(20,0,40,0.8);
            border: 2px solid rgba(180,77,255,0.4);
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .product-card:hover {
            border-color: #b44dff;
            transform: translateY(-5px);
        }

        .product-image {
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #1a0030, #2a0050);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 64px;
        }

        .product-info {
            padding: 12px;
            text-align: center;
        }

        .product-name {
            color: #b44dff;
            font-weight: bold;
        }

        .sizes-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin: 20px 0;
        }

        .size-card {
            background: rgba(20,0,40,0.8);
            border: 2px solid #7b6bff;
            padding: 15px;
            text-align: center;
            cursor: pointer;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        .size-card.selected {
            background: linear-gradient(135deg, #7b6bff, #b44dff);
            color: #0a0010;
        }

        .country-item, .city-item, .shop-item {
            background: rgba(20,0,40,0.8);
            border: 1px solid rgba(180,77,255,0.3);
            padding: 15px;
            margin: 10px 0;
            cursor: pointer;
            border-radius: 5px;
        }

        .country-item:hover, .city-item:hover, .shop-item:hover {
            border-color: #b44dff;
            background: rgba(180,77,255,0.1);
        }

        .back-btn {
            position: fixed;
            top: 20px;
            left: 20px;
            background: rgba(20,0,40,0.9);
            border: 1px solid #b44dff;
            color: #b44dff;
            padding: 10px 20px;
            cursor: pointer;
            z-index: 1001;
            border-radius: 5px;
        }

        .text-center { text-align: center; }
        .pt-60 { padding-top: 60px; }
        .mb-10 { margin-bottom: 10px; }
        .mb-20 { margin-bottom: 20px; }
        .mb-30 { margin-bottom: 30px; }
        .mt-20 { margin-top: 20px; }
        .mt-30 { margin-top: 30px; }

        .admin-tab {
            display: inline-block;
            padding: 8px 16px;
            margin: 5px;
            background: rgba(20,0,40,0.8);
            border: 1px solid #b44dff;
            border-radius: 5px;
            cursor: pointer;
        }
        .admin-tab.active {
            background: #b44dff;
            color: #0a0010;
        }
        .admin-section {
            display: none;
        }
        .admin-section.active {
            display: block;
        }
        input, textarea {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            background: rgba(20,0,40,0.8);
            border: 1px solid #b44dff;
            color: #b44dff;
            border-radius: 5px;
            font-family: monospace;
        }
        label {
            color: #7b6bff;
            font-size: 12px;
            display: block;
        }
        .wallet-addr {
            font-size: 11px;
            word-break: break-all;
            background: rgba(0,0,0,0.5);
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
        }
        .copy-btn {
            background: #2a0050;
            border: 1px solid #ff6b9d;
            color: #ff6b9d;
            padding: 5px 10px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 11px;
            margin-left: 10px;
        }
        .order-item {
            border-bottom: 1px solid #333;
            padding: 10px;
            font-size: 12px;
        }
        .order-item span {
            color: #ff6b9d;
        }
        .delete-orders-btn {
            background: rgba(200,0,0,0.3);
            border-color: #ff4444;
            color: #ff4444;
            margin-top: 20px;
        }
        .delete-orders-btn:hover {
            background: #ff4444;
            color: #0a0010;
        }
    </style>
</head>
<body>
    <div class="scanlines"></div>
    <button class="back-btn" onclick="goBack()" style="display: none;" id="backBtn">◄ НАЗАД</button>

    <!-- ГЛАВНАЯ -->
    <div class="page active" id="homePage">
        <div class="text-center pt-60">
            <div class="neon-text" style="font-size: 48px;">NEON</div>
            <div style="color: #ff6b9d; font-size: 36px; font-weight: bold;">MARKETPLACE</div>
            <div class="cyber-card mb-30 mt-20">
                <p style="color: #ddd;">Добро пожаловать в магазин будущего</p>
            </div>
            <button class="cyber-btn" onclick="enterStore()">▶ НАЧАТЬ ПОКУПКИ</button>
            <div style="margin-top: 20px; font-size: 11px; color: rgba(180,77,255,0.5);" id="adminHint"></div>
        </div>
    </div>

    <!-- АДМИН-ПАНЕЛЬ -->
    <div class="page" id="adminPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-20">ADMIN PANEL</div>
            <div id="adminTabs">
                <span class="admin-tab active" onclick="showAdminSection('bank')">🏦 БАНК</span>
                <span class="admin-tab" onclick="showAdminSection('crypto')">💎 КРИПТО</span>
                <span class="admin-tab" onclick="showAdminSection('orders')">📋 ЗАКАЗЫ</span>
            </div>
            
            <div id="bankSection" class="admin-section active">
                <div class="cyber-card">
                    <label>🔗 ССЫЛКА НА ОПЛАТУ (SBP / QR / Платёжный шлюз)</label>
                    <input type="text" id="bankLinkInput" placeholder="https://payment.example.com/..." value="">
                    <button class="cyber-btn" onclick="saveBankLink()">💾 СОХРАНИТЬ ССЫЛКУ</button>
                    <div style="margin-top: 10px; color: #7b6bff; font-size: 12px;" id="currentBankLink"></div>
                </div>
                <div class="cyber-card mt-20">
                    <div style="color: #ff6b9d;">ℹ️ Поддерживаются любые платёжные ссылки:</div>
                    <div style="font-size: 11px;">• СБП QR-код<br>• Ссылка на оплату по реквизитам<br>• Платёжный шлюз (PayKeeper, UnitPay и др.)</div>
                </div>
            </div>
            
            <div id="cryptoSection" class="admin-section">
                <div class="cyber-card">
                    <label>💰 USDT (TRC20 / ERC20 / BEP20)</label>
                    <input type="text" id="usdtWallet" placeholder="TXXXX... или 0xXXXX...">
                    <button class="cyber-btn" onclick="saveCryptoWallet('USDT')">💾 СОХРАНИТЬ USDT</button>
                </div>
                <div class="cyber-card">
                    <label>₿ BITCOIN (BTC)</label>
                    <input type="text" id="btcWallet" placeholder="bc1... или 1... или 3...">
                    <button class="cyber-btn" onclick="saveCryptoWallet('BTC')">💾 СОХРАНИТЬ BTC</button>
                </div>
                <div class="cyber-card">
                    <label>🔒 MONERO (XMR)</label>
                    <input type="text" id="xmrWallet" placeholder="48...">
                    <button class="cyber-btn" onclick="saveCryptoWallet('XMR')">💾 СОХРАНИТЬ XMR</button>
                </div>
                <div class="cyber-card">
                    <label>⚡ LITECOIN (LTC)</label>
                    <input type="text" id="ltcWallet" placeholder="L... или M...">
                    <button class="cyber-btn" onclick="saveCryptoWallet('LTC')">💾 СОХРАНИТЬ LTC</button>
                </div>
            </div>
            
            <div id="ordersSection" class="admin-section">
                <div class="cyber-card" id="adminOrdersList">
                    <div style="color: #999;">Загрузка...</div>
                </div>
                <button class="cyber-btn delete-orders-btn" onclick="clearAllOrders()">🗑 УДАЛИТЬ ВСЕ ЗАКАЗЫ</button>
            </div>
            
            <button class="cyber-btn mt-20" onclick="showPage('homePage')">◄ В МАГАЗИН</button>
        </div>
    </div>

    <!-- СТРАНЫ -->
    <div class="page" id="countryPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-30">ВЫБЕРИТЕ СТРАНУ</div>
            <div id="countriesContainer"></div>
        </div>
    </div>

    <!-- ГОРОДА -->
    <div class="page" id="cityPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-10">ВЫБЕРИТЕ ГОРОД</div>
            <div id="citiesContainer"></div>
        </div>
    </div>

    <!-- КАТАЛОГ -->
    <div class="page" id="catalogPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-10">КАТАЛОГ</div>
            <div class="products-grid" id="productsContainer"></div>
        </div>
    </div>

    <!-- РАЗМЕРЫ -->
    <div class="page" id="sizePage">
        <div class="text-center pt-60">
            <div class="neon-text mb-10" id="selectedProductTitle">ВЫБОР РАЗМЕРА</div>
            <div class="sizes-grid" id="sizesContainer"></div>
            <button class="cyber-btn mt-30" id="confirmSizeBtn" disabled onclick="goToShops()">ВЫБРАТЬ РАЗМЕР</button>
        </div>
    </div>

    <!-- ТОЧКИ ВЫДАЧИ -->
    <div class="page" id="shopPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-10">ТОЧКИ ВЫДАЧИ</div>
            <div class="cyber-card mb-20" id="orderSummary"></div>
            <div id="shopsContainer"></div>
        </div>
    </div>

    <!-- ОПЛАТА -->
    <div class="page" id="paymentPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-30">СПОСОБ ОПЛАТЫ</div>
            <div class="cyber-card mb-15" id="bankPaymentBtn" onclick="selectBankPayment()">
                <div style="font-size: 20px;">🏦 БАНКОВСКИЙ ПЕРЕВОД</div>
                <div style="font-size: 12px; color: #999;">По ссылке / QR</div>
            </div>
            <div class="cyber-card mb-15" onclick="showCryptoSelection()">
                <div style="font-size: 20px;">💎 КРИПТОВАЛЮТА</div>
                <div style="font-size: 12px; color: #999;">USDT / BTC / XMR / LTC</div>
            </div>
        </div>
    </div>

    <!-- ВЫБОР КРИПТЫ -->
    <div class="page" id="cryptoSelectPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-30">ВЫБЕРИТЕ КРИПТОВАЛЮТУ</div>
            <div id="cryptoListContainer"></div>
        </div>
    </div>

    <!-- ОПЛАТА КРИПТОЙ -->
    <div class="page" id="cryptoPaymentPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-20">ОПЛАТА КРИПТОВАЛЮТОЙ</div>
            <div class="cyber-card mb-20">
                <div style="color: #b44dff;">Сумма к оплате:</div>
                <div style="color: #ff6b9d; font-size: 32px;" id="cryptoAmountRub"></div>
                <div style="color: #7b6bff; font-size: 18px;" id="cryptoAmountCoin"></div>
            </div>
            <div class="cyber-card mb-20">
                <div style="color: #b44dff;">Кошелёк получателя:</div>
                <div class="wallet-addr" id="cryptoWalletAddr"></div>
                <button class="copy-btn" onclick="copyWallet()">📋 КОПИРОВАТЬ</button>
            </div>
            <button class="cyber-btn" onclick="confirmCryptoPayment()">✅ Я ОПЛАТИЛ</button>
        </div>
    </div>

    <!-- ОПЛАТА БАНКОМ (ССЫЛКА) -->
    <div class="page" id="bankPaymentPage">
        <div class="text-center pt-60">
            <div class="neon-text mb-20">ОПЛАТА ПО ССЫЛКЕ</div>
            <div class="cyber-card mb-20">
                <div style="color: #b44dff;">Сумма:</div>
                <div style="color: #ff6b9d; font-size: 32px;" id="bankAmountRub"></div>
            </div>
            <div class="cyber-card mb-20">
                <div style="color: #b44dff;">Ссылка для оплаты:</div>
                <div class="wallet-addr" id="bankLinkDisplay"></div>
                <button class="copy-btn" onclick="copyBankLink()">📋 КОПИРОВАТЬ ССЫЛКУ</button>
                <button class="cyber-btn mt-20" onclick="openBankLink()">🔗 ОТКРЫТЬ ССЫЛКУ</button>
            </div>
            <button class="cyber-btn" onclick="confirmBankPayment()">✅ Я ОПЛАТИЛ</button>
        </div>
    </div>

    <!-- УСПЕХ -->
    <div class="page" id="successPage">
        <div class="text-center pt-60">
            <div style="font-size: 72px;">✅</div>
            <div class="neon-text mb-30">ЗАКАЗ ОФОРМЛЕН!</div>
            <div class="cyber-card mb-20">
                <div id="successOrderNumber" style="color: #b44dff;"></div>
                <div style="color: #7b6bff;">Ожидайте звонка оператора</div>
            </div>
            <button class="cyber-btn" onclick="resetAndGoHome()">🏠 НА ГЛАВНУЮ</button>
            <button class="cyber-btn" onclick="window.Telegram.WebApp.close()">❌ ЗАКРЫТЬ</button>
        </div>
    </div>

    <script>
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand();
        
        let userId = tg.initDataUnsafe?.user?.id || 0;
        let isAdmin = false;
        
        // Администраторы (можно добавить свои ID)
        const ADMIN_IDS = []; // Добавьте сюда свой Telegram ID, например: [123456789]
        
        // ========== ЛОКАЛЬНОЕ ХРАНИЛИЩЕ ==========
        function loadSettings() {
            const defaultSettings = {
                bankLink: "",
                cryptoWallets: { USDT: "", BTC: "", XMR: "", LTC: "" },
                orders: []
            };
            const saved = localStorage.getItem('neon_store_settings');
            if (saved) {
                return JSON.parse(saved);
            }
            return defaultSettings;
        }
        
        function saveSettings(settings) {
            localStorage.setItem('neon_store_settings', JSON.stringify(settings));
        }
        
        let settings = loadSettings();
        
        // ========== ДАННЫЕ МАГАЗИНА ==========
        const storeData = {
            countries: {
                'RU': { name: 'РОССИЯ', cities: {
                    'moscow': { name: 'МОСКВА', shops: [
                        { id: 'msk1', name: 'Москва Центр', address: 'ул. Тверская, 15', phone: '+7(999)123-45-67' },
                        { id: 'msk2', name: 'Москва Юг', address: 'ул. Варшавская, 42', phone: '+7(999)234-56-78' }
                    ]},
                    'spb': { name: 'САНКТ-ПЕТЕРБУРГ', shops: [
                        { id: 'spb1', name: 'СПб Центр', address: 'Невский пр., 100', phone: '+7(999)456-78-90' }
                    ]}
                }},
                'KZ': { name: 'КАЗАХСТАН', cities: {
                    'almaty': { name: 'АЛМАТЫ', shops: [
                        { id: 'alm1', name: 'Алматы Центр', address: 'пр. Назарбаева, 50', phone: '+7(701)123-45-67' }
                    ]},
                    'astana': { name: 'АСТАНА', shops: [
                        { id: 'ast1', name: 'Астана Центр', address: 'ул. Туран, 25', phone: '+7(701)765-43-21' }
                    ]}
                }},
                'BY': { name: 'БЕЛАРУСЬ', cities: {
                    'minsk': { name: 'МИНСК', shops: [
                        { id: 'mnk1', name: 'Минск Центр', address: 'пр. Независимости, 50', phone: '+375(29)123-45-67' }
                    ]}
                }},
                'TR': { name: 'ТУРЦИЯ', cities: {
                    'istanbul': { name: 'СТАМБУЛ', shops: [
                        { id: 'ist1', name: 'Стамбул Центр', address: 'Istiklal Cd., 100', phone: '+90(555)123-45-67' }
                    ]}
                }}
            },
            products: [
                { id: 'hoodie', name: 'CYBER HOODIE', image: '🧥', sizes: { 'XS': 8500, 'S': 10500, 'M': 12500, 'L': 14500, 'XL': 16500 } },
                { id: 'tshirt', name: 'GLITCH T-SHIRT', image: '👕', sizes: { 'S': 3500, 'M': 4500, 'L': 5500, 'XL': 6500 } },
                { id: 'jacket', name: 'NEON BOMBER', image: '🧥', sizes: { 'S': 12500, 'M': 14500, 'L': 16500, 'XL': 18500 } }
            ]
        };
        
        const state = {
            history: ['homePage'],
            selectedCountry: null,
            selectedCity: null,
            selectedProduct: null,
            selectedSize: null,
            selectedPrice: null,
            selectedShop: null,
            selectedCrypto: null
        };
        
        // ========== ПРОВЕРКА АДМИНА ==========
        function checkAdmin() {
            isAdmin = ADMIN_IDS.includes(userId);
            if (isAdmin) {
                document.getElementById('adminHint').innerHTML = '<span style="color:#ff6b9d;">👑 Вы вошли как администратор (нажмите на логотип для входа в админку)</span>';
            }
            return isAdmin;
        }
        
        function enterStore() {
            if (isAdmin) {
                if (confirm('Вы вошли как администратор. Открыть панель управления?')) {
                    showAdminPanel();
                    return;
                }
            }
            showPage('countryPage');
        }
        
        function showAdminPanel() {
            updateAdminUI();
            showPage('adminPage');
        }
        
        // Админ-функции
        function updateAdminUI() {
            document.getElementById('bankLinkInput').value = settings.bankLink || '';
            document.getElementById('currentBankLink').innerHTML = `Текущая ссылка: <br><span style="font-size:11px; word-break:break-all;">${settings.bankLink || '❌ Не установлена'}</span>`;
            document.getElementById('usdtWallet').value = settings.cryptoWallets.USDT || '';
            document.getElementById('btcWallet').value = settings.cryptoWallets.BTC || '';
            document.getElementById('xmrWallet').value = settings.cryptoWallets.XMR || '';
            document.getElementById('ltcWallet').value = settings.cryptoWallets.LTC || '';
            updateOrdersList();
        }
        
        function updateOrdersList() {
            const container = document.getElementById('adminOrdersList');
            if (!container) return;
            if (!settings.orders.length) {
                container.innerHTML = '<div style="color:#999;">📭 Нет заказов</div>';
                return;
            }
            let html = '';
            for (let o of [...settings.orders].reverse()) {
                html += `<div class="order-item">
                    <div>🎫 <span>#${o.id}</span> | ${o.date}</div>
                    <div>📦 ${o.product} | ${o.size} | ${o.price.toLocaleString()} ₽</div>
                    <div>📍 ${o.shop}</div>
                    <div>💳 ${o.paymentMethod}</div>
                </div>`;
            }
            container.innerHTML = html;
        }
        
        function saveBankLink() {
            const link = document.getElementById('bankLinkInput').value;
            settings.bankLink = link;
            saveSettings(settings);
            updateAdminUI();
            alert('✅ Ссылка для оплаты сохранена!');
        }
        
        function saveCryptoWallet(currency) {
            let wallet = '';
            if (currency === 'USDT') wallet = document.getElementById('usdtWallet').value;
            if (currency === 'BTC') wallet = document.getElementById('btcWallet').value;
            if (currency === 'XMR') wallet = document.getElementById('xmrWallet').value;
            if (currency === 'LTC') wallet = document.getElementById('ltcWallet').value;
            if (!wallet) {
                alert('Введите адрес кошелька');
                return;
            }
            settings.cryptoWallets[currency] = wallet;
            saveSettings(settings);
            updateAdminUI();
            alert(`✅ Кошелёк ${currency} сохранён!`);
        }
        
        function clearAllOrders() {
            if (confirm('⚠️ ВНИМАНИЕ! Это действие удалит ВСЕ заказы без возможности восстановления. Продолжить?')) {
                settings.orders = [];
                saveSettings(settings);
                updateOrdersList();
                alert('🗑 Все заказы удалены');
            }
        }
        
        function showAdminSection(section) {
            document.querySelectorAll('.admin-section').forEach(el => el.classList.remove('active'));
            document.getElementById(section + 'Section').classList.add('active');
            document.querySelectorAll('.admin-tab').forEach((tab, i) => {
                tab.classList.remove('active');
                if ((section === 'bank' && i === 0) || (section === 'crypto' && i === 1) || (section === 'orders' && i === 2)) {
                    tab.classList.add('active');
                }
            });
        }
        
        // ========== НАВИГАЦИЯ ==========
        function showPage(pageId) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(pageId).classList.add('active');
            state.history.push(pageId);
            document.getElementById('backBtn').style.display = pageId === 'homePage' ? 'none' : 'block';
            window.scrollTo(0, 0);
        }
        
        function goBack() {
            if (state.history.length > 1) {
                state.history.pop();
                const prev = state.history[state.history.length - 1];
                document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
                document.getElementById(prev).classList.add('active');
                if (prev === 'homePage') document.getElementById('backBtn').style.display = 'none';
            }
        }
        
        function resetAndGoHome() {
            // Сброс состояния
            state.selectedCountry = null;
            state.selectedCity = null;
            state.selectedProduct = null;
            state.selectedSize = null;
            state.selectedPrice = null;
            state.selectedShop = null;
            state.selectedCrypto = null;
            state.history = ['homePage'];
            showPage('homePage');
        }
        
        // ========== СТРАНЫ ==========
        function renderCountries() {
            const container = document.getElementById('countriesContainer');
            container.innerHTML = '';
            for (let [code, country] of Object.entries(storeData.countries)) {
                const div = document.createElement('div');
                div.className = 'country-item';
                div.onclick = () => selectCountry(code);
                div.innerHTML = `<div style="font-size:20px;">${country.name}</div>`;
                container.appendChild(div);
            }
        }
        
        function selectCountry(code) {
            state.selectedCountry = code;
            const country = storeData.countries[code];
            const container = document.getElementById('citiesContainer');
            container.innerHTML = '';
            for (let [cityCode, city] of Object.entries(country.cities)) {
                const div = document.createElement('div');
                div.className = 'city-item';
                div.onclick = () => selectCity(cityCode);
                div.innerHTML = `<div style="font-size:20px;">🏙 ${city.name}</div><div style="font-size:12px;">${city.shops.length} точки</div>`;
                container.appendChild(div);
            }
            showPage('cityPage');
        }
        
        function selectCity(cityCode) {
            state.selectedCity = cityCode;
            const container = document.getElementById('productsContainer');
            container.innerHTML = '';
            storeData.products.forEach(product => {
                const div = document.createElement('div');
                div.className = 'product-card';
                div.onclick = () => selectProduct(product.id);
                div.innerHTML = `<div class="product-image">${product.image}</div><div class="product-info"><div class="product-name">${product.name}</div></div>`;
                container.appendChild(div);
            });
            showPage('catalogPage');
        }
        
        function selectProduct(productId) {
            state.selectedProduct = productId;
            const product = storeData.products.find(p => p.id === productId);
            document.getElementById('selectedProductTitle').textContent = product.name;
            const container = document.getElementById('sizesContainer');
            container.innerHTML = '';
            Object.entries(product.sizes).forEach(([size, price]) => {
                const div = document.createElement('div');
                div.className = 'size-card';
                div.onclick = function() { selectSize(size, price, this); };
                div.innerHTML = `<div>${size}</div><div>${price.toLocaleString()} ₽</div>`;
                container.appendChild(div);
            });
            state.selectedSize = null;
            document.getElementById('confirmSizeBtn').disabled = true;
            showPage('sizePage');
        }
        
        function selectSize(size, price, element) {
            state.selectedSize = size;
            state.selectedPrice = price;
            document.querySelectorAll('.size-card').forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
            const btn = document.getElementById('confirmSizeBtn');
            btn.disabled = false;
            btn.textContent = `ДАЛЕЕ ▶ ${price.toLocaleString()} ₽`;
        }
        
        function goToShops() {
            if (!state.selectedSize) return;
            const product = storeData.products.find(p => p.id === state.selectedProduct);
            const country = storeData.countries[state.selectedCountry];
            const city = country.cities[state.selectedCity];
            document.getElementById('orderSummary').innerHTML = `
                <div>📦 Товар: <span style="color:#b44dff;">${product.name}</span></div>
                <div>📏 Размер: <span style="color:#7b6bff;">${state.selectedSize}</span></div>
                <div>💰 Цена: <span style="color:#ff6b9d;">${state.selectedPrice.toLocaleString()} ₽</span></div>
            `;
            const container = document.getElementById('shopsContainer');
            container.innerHTML = '';
            city.shops.forEach(shop => {
                const div = document.createElement('div');
                div.className = 'shop-item';
                div.onclick = () => selectShop(shop);
                div.innerHTML = `<div style="color:#b44dff;">📍 ${shop.name}</div><div style="color:#999;">${shop.address}</div><div style="color:#7b6bff; font-size:11px;">📞 ${shop.phone}</div>`;
                container.appendChild(div);
            });
            showPage('shopPage');
        }
        
        function selectShop(shop) {
            state.selectedShop = shop;
            showPage('paymentPage');
        }
        
        // ========== ОПЛАТА ==========
        function showCryptoSelection() {
            const container = document.getElementById('cryptoListContainer');
            const cryptos = ['USDT', 'BTC', 'XMR', 'LTC'];
            container.innerHTML = '';
            let hasAny = false;
            for (let crypto of cryptos) {
                if (settings.cryptoWallets[crypto] && settings.cryptoWallets[crypto].trim() !== '') {
                    hasAny = true;
                    const div = document.createElement('div');
                    div.className = 'cyber-card';
                    div.onclick = () => selectCrypto(crypto);
                    let icon = crypto === 'USDT' ? '💵' : crypto === 'BTC' ? '₿' : crypto === 'XMR' ? '🔒' : '⚡';
                    div.innerHTML = `<div style="font-size:24px;">${icon} ${crypto}</div>`;
                    container.appendChild(div);
                }
            }
            if (!hasAny) {
                container.innerHTML = '<div class="cyber-card">❌ Крипто-кошельки не настроены администратором</div>';
            } else {
                showPage('cryptoSelectPage');
            }
        }
        
        // Курсы валют (примерные, можно менять)
        const cryptoRates = { USDT: 100, BTC: 6000000, XMR: 15000, LTC: 7000 };
        
        function selectCrypto(currency) {
            state.selectedCrypto = currency;
            const wallet = settings.cryptoWallets[currency];
            document.getElementById('cryptoAmountRub').textContent = state.selectedPrice.toLocaleString() + ' ₽';
            let amount = (state.selectedPrice / cryptoRates[currency]).toFixed(currency === 'BTC' ? 6 : 4);
            document.getElementById('cryptoAmountCoin').textContent = `${amount} ${currency}`;
            document.getElementById('cryptoWalletAddr').textContent = wallet;
            showPage('cryptoPaymentPage');
        }
        
        function copyWallet() {
            const addr = document.getElementById('cryptoWalletAddr').textContent;
            navigator.clipboard.writeText(addr);
            alert('📋 Кошелёк скопирован!');
            tg.HapticFeedback?.notificationOccurred('success');
        }
        
        function confirmCryptoPayment() {
            sendOrder('Криптовалюта (' + state.selectedCrypto + ')');
        }
        
        function selectBankPayment() {
            if (!settings.bankLink || settings.bankLink.trim() === '') {
                alert('❌ Ссылка на оплату не настроена администратором');
                return;
            }
            document.getElementById('bankAmountRub').textContent = state.selectedPrice.toLocaleString() + ' ₽';
            document.getElementById('bankLinkDisplay').textContent = settings.bankLink;
            showPage('bankPaymentPage');
        }
        
        function copyBankLink() {
            navigator.clipboard.writeText(settings.bankLink);
            alert('📋 Ссылка скопирована!');
            tg.HapticFeedback?.notificationOccurred('success');
        }
        
        function openBankLink() {
            window.open(settings.bankLink, '_blank');
        }
        
        function confirmBankPayment() {
            sendOrder('Банковский перевод');
        }
        
        function sendOrder(paymentMethod) {
            const product = storeData.products.find(p => p.id === state.selectedProduct);
            const country = storeData.countries[state.selectedCountry];
            const city = country.cities[state.selectedCity];
            
            const orderId = settings.orders.length + 1;
            const newOrder = {
                id: orderId,
                userId: userId,
                product: product.name,
                size: state.selectedSize,
                price: state.selectedPrice,
                shop: state.selectedShop.name,
                country: country.name,
                city: city.name,
                paymentMethod: paymentMethod,
                date: new Date().toLocaleString('ru-RU')
            };
            
            settings.orders.push(newOrder);
            saveSettings(settings);
            
            document.getElementById('successOrderNumber').innerHTML = `Номер заказа: #NEON-${String(orderId).padStart(4, '0')}`;
            showPage('successPage');
            
            tg.HapticFeedback?.notificationOccurred('success');
            
            // Если есть Telegram, отправим уведомление (опционально)
            if (tg.sendData) {
                tg.sendData(JSON.stringify({ action: 'order_created', order: newOrder }));
            }
        }
        
        // ========== ИНИЦИАЛИЗАЦИЯ ==========
        renderCountries();
        checkAdmin();
        
        // Клик по логотипу для админа
        document.querySelector('.neon-text')?.addEventListener('click', () => {
            if (isAdmin) {
                showAdminPanel();
            }
        });
    </script>
</body>
</html>
