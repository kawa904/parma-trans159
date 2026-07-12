from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ===== ГЛАВНАЯ =====
@app.get("/", response_class=HTMLResponse)
async def index():
    html = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>ПАРМА ТРАНС — Перевозки по Пермскому краю</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            background: #0a0f1e;
            min-height: 100vh;
            padding: 20px;
            position: relative;
            padding-bottom: 100px;
        }

        /* ===== ЧАСТИЦЫ ===== */
        #particles-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
        }

        /* ===== КОНТЕЙНЕР ===== */
        .container {
            max-width: 600px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        /* ===== КАРТОЧКА ===== */
        .glass-card {
            position: relative;
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-radius: 48px;
            padding: 40px 32px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 
                0 30px 80px rgba(0, 0, 0, 0.6),
                inset 0 0 80px rgba(245, 200, 66, 0.04),
                0 0 0 1px rgba(255, 255, 255, 0.04) inset;
            margin-bottom: 20px;
            transition: all 0.4s ease;
        }

        .glass-card::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            border-radius: 50px;
            background: linear-gradient(135deg, rgba(245, 200, 66, 0.3), transparent 40%, transparent 60%, rgba(245, 200, 66, 0.15));
            z-index: -1;
            animation: borderGlow 4s ease-in-out infinite alternate;
        }

        @keyframes borderGlow {
            0% { opacity: 0.4; }
            100% { opacity: 1; }
        }

        /* ===== АКЦИЯ ===== */
        .promo-banner {
            background: linear-gradient(135deg, rgba(245, 200, 66, 0.15), rgba(245, 200, 66, 0.05));
            border: 1px solid rgba(245, 200, 66, 0.2);
            border-radius: 16px;
            padding: 12px 20px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
            animation: pulseBanner 2s ease-in-out infinite;
        }

        @keyframes pulseBanner {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }

        .promo-banner i {
            color: #f5c842;
            font-size: 24px;
            animation: shake 1s ease-in-out infinite;
        }

        @keyframes shake {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(-10deg); }
            75% { transform: rotate(10deg); }
        }

        .promo-banner .promo-text {
            font-size: 15px;
            font-weight: 700;
            color: #f5c842;
        }

        .promo-banner .promo-desc {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.5);
        }

        /* ===== ЛОГО ===== */
        .logo-section {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 16px;
        }

        .logo-icon {
            font-size: 44px;
            background: linear-gradient(135deg, #f5c842, #f7b731);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 30px rgba(245, 200, 66, 0.25));
            animation: floatIcon 3s ease-in-out infinite;
        }

        @keyframes floatIcon {
            0%, 100% { transform: translateY(0px) rotate(-2deg); }
            50% { transform: translateY(-6px) rotate(2deg); }
        }

        .logo-text h1 {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: 2px;
            background: linear-gradient(135deg, #ffffff 60%, #f5c842 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
        }

        .logo-text span {
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.35);
            margin-top: 2px;
        }

        /* ===== БЭЙДЖ ===== */
        .badge {
            display: inline-block;
            background: rgba(245, 200, 66, 0.12);
            padding: 6px 18px;
            border-radius: 40px;
            font-size: 11px;
            font-weight: 600;
            color: #f5c842;
            letter-spacing: 1px;
            text-transform: uppercase;
            border: 1px solid rgba(245, 200, 66, 0.12);
            margin-bottom: 12px;
        }

        .badge i { margin-right: 8px; }

        /* ===== ЗАГОЛОВОК ===== */
        .hero-title {
            font-size: 34px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.15;
            margin-bottom: 4px;
        }

        .hero-title span { color: #f5c842; }

        .hero-sub {
            color: rgba(255, 255, 255, 0.5);
            font-size: 15px;
            line-height: 1.6;
            margin-bottom: 20px;
            font-weight: 400;
        }

        /* ===== ОСОБЕННОСТИ ===== */
        .features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 20px;
        }

        .feature-item {
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255, 255, 255, 0.03);
            padding: 10px 14px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.04);
            transition: all 0.3s ease;
        }

        .feature-item:hover {
            background: rgba(245, 200, 66, 0.06);
            border-color: rgba(245, 200, 66, 0.12);
            transform: translateY(-2px);
        }

        .feature-item i {
            font-size: 18px;
            color: #f5c842;
            width: 28px;
            text-align: center;
        }

        .feature-item span {
            font-size: 13px;
            font-weight: 600;
            color: rgba(255, 255, 255, 0.8);
        }

        .feature-item small {
            font-size: 10px;
            color: rgba(255, 255, 255, 0.3);
            display: block;
            font-weight: 400;
        }

        /* ===== СТАТИСТИКА ===== */
        .stats {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
            padding: 16px 0;
            border-top: 1px solid rgba(255, 255, 255, 0.04);
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        }

        .stat-item {
            text-align: center;
        }

        .stat-item .num {
            font-size: 24px;
            font-weight: 800;
            color: #f5c842;
            display: block;
            letter-spacing: 0.5px;
        }

        .stat-item .label {
            font-size: 10px;
            color: rgba(255, 255, 255, 0.3);
            font-weight: 400;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* ===== КАЛЬКУЛЯТОР ===== */
        .calculator {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.04);
        }

        .calculator-title {
            color: #f5c842;
            font-weight: 700;
            font-size: 16px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .calc-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 10px;
        }

        .calc-input {
            padding: 12px 14px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            background: rgba(255, 255, 255, 0.04);
            color: #ffffff;
            font-size: 14px;
            font-family: 'Inter', sans-serif;
            outline: none;
            transition: 0.3s;
            width: 100%;
        }

        .calc-input:focus {
            border-color: rgba(245, 200, 66, 0.3);
            background: rgba(255, 255, 255, 0.06);
        }

        .calc-input::placeholder {
            color: rgba(255, 255, 255, 0.2);
        }

        .calc-result {
            text-align: center;
            padding: 12px;
            background: rgba(245, 200, 66, 0.06);
            border-radius: 12px;
            border: 1px solid rgba(245, 200, 66, 0.1);
            color: #f5c842;
            font-weight: 700;
            font-size: 18px;
            margin-top: 4px;
        }

        /* ===== ОТЗЫВЫ ===== */
        .reviews {
            margin-bottom: 20px;
        }

        .review-item {
            background: rgba(255, 255, 255, 0.03);
            padding: 16px 18px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.04);
            margin-bottom: 10px;
        }

        .review-item .review-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 6px;
        }

        .review-item .review-avatar {
            font-size: 32px;
        }

        .review-item .review-name {
            font-weight: 700;
            color: #ffffff;
            font-size: 15px;
        }

        .review-item .review-city {
            font-size: 12px;
            color: rgba(255, 255, 255, 0.3);
        }

        .review-item .review-text {
            color: rgba(255, 255, 255, 0.6);
            font-size: 14px;
            line-height: 1.5;
        }

        .review-item .review-stars {
            color: #f5c842;
            font-size: 14px;
            margin-top: 4px;
        }

        /* ===== КОНТАКТЫ ===== */
        .contacts {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 16px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255, 255, 255, 0.03);
            padding: 12px 14px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.04);
            transition: 0.3s;
        }

        .contact-item:hover {
            background: rgba(245, 200, 66, 0.06);
            border-color: rgba(245, 200, 66, 0.12);
        }

        .contact-item i {
            font-size: 18px;
            color: #f5c842;
            width: 24px;
            text-align: center;
        }

        .contact-item .contact-text {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.7);
        }

        .contact-item .contact-label {
            font-size: 10px;
            color: rgba(255, 255, 255, 0.2);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* ===== ФОРМА ===== */
        .form-group {
            position: relative;
            margin-bottom: 14px;
        }

        .form-group i {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: rgba(255, 255, 255, 0.2);
            font-size: 16px;
            transition: all 0.3s ease;
            pointer-events: none;
        }

        .form-group textarea ~ i {
            top: 20px;
            transform: none;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 14px 16px 14px 48px;
            border-radius: 16px;
            border: 1.5px solid rgba(255, 255, 255, 0.06);
            background: rgba(255, 255, 255, 0.04);
            color: #ffffff;
            font-size: 15px;
            font-family: 'Inter', sans-serif;
            transition: all 0.3s ease;
            outline: none;
        }

        .form-group textarea {
            min-height: 80px;
            resize: vertical;
            padding-top: 18px;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            border-color: rgba(245, 200, 66, 0.4);
            background: rgba(255, 255, 255, 0.06);
            box-shadow: 0 0 0 4px rgba(245, 200, 66, 0.06);
        }

        .form-group input:focus ~ i,
        .form-group textarea:focus ~ i {
            color: #f5c842;
        }

        .form-group input::placeholder,
        .form-group textarea::placeholder {
            color: rgba(255, 255, 255, 0.2);
            font-weight: 400;
        }

        /* ===== ЧЕКБОКСЫ ===== */
        .checkbox-group {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin: 12px 0;
            font-size: 13px;
            color: rgba(255, 255, 255, 0.5);
            line-height: 1.4;
        }

        .checkbox-group input[type="checkbox"] {
            width: 20px;
            height: 20px;
            flex-shrink: 0;
            margin-top: 1px;
            accent-color: #f5c842;
            cursor: pointer;
            border-radius: 6px;
        }

        .checkbox-group a {
            color: #f5c842;
            text-decoration: none;
            border-bottom: 1px dashed rgba(245, 200, 66, 0.25);
            transition: border-color 0.3s ease;
        }

        .checkbox-group a:hover { border-color: #f5c842; }
        .required { color: #f5c842; }

        /* ===== КНОПКИ ===== */
        .submit-btn {
            width: 100%;
            padding: 16px;
            border: none;
            border-radius: 60px;
            font-size: 17px;
            font-weight: 800;
            font-family: 'Inter', sans-serif;
            color: #0a0f1e;
            background: linear-gradient(135deg, #f5c842, #f7b731, #e8a820);
            background-size: 200% 200%;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 30px rgba(245, 200, 66, 0.25);
            margin-top: 4px;
            letter-spacing: 0.5px;
            animation: gradientShift 3s ease-in-out infinite;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .submit-btn:hover {
            transform: translateY(-3px) scale(1.01);
            box-shadow: 0 12px 40px rgba(245, 200, 66, 0.35);
        }

        .submit-btn:active { transform: translateY(0px) scale(0.99); }
        .submit-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none !important;
            box-shadow: 0 8px 30px rgba(245, 200, 66, 0.1) !important;
        }

        /* ===== СТАТУС ===== */
        #status {
            margin-top: 14px;
            text-align: center;
            font-weight: 600;
            font-size: 14px;
            min-height: 24px;
        }
        .success { color: #81c784; }
        .error { color: #ef9a9a; }

        /* ===== ФУТЕР ===== */
        .footer {
            margin-top: 20px;
            padding-top: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.04);
            text-align: center;
            font-size: 12px;
            color: rgba(255, 255, 255, 0.2);
        }

        .footer a {
            color: rgba(255, 255, 255, 0.3);
            text-decoration: none;
            transition: color 0.3s ease;
            margin: 0 8px;
        }

        .footer a:hover { color: #f5c842; }

        /* ===== ЛИПКАЯ КНОПКА ===== */
        .sticky-bottom {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 16px 20px;
            background: rgba(10, 15, 30, 0.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            display: flex;
            gap: 10px;
            z-index: 100;
            flex-wrap: wrap;
        }

        .sticky-btn {
            flex: 1;
            padding: 14px 16px;
            border: none;
            border-radius: 16px;
            font-size: 15px;
            font-weight: 700;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            min-width: 120px;
        }

        .sticky-btn.call-btn {
            background: linear-gradient(135deg, #25d366, #128c7e);
            color: #ffffff;
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.3);
        }

        .sticky-btn.whatsapp-btn {
            background: linear-gradient(135deg, #25d366, #128c7e);
            color: #ffffff;
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.3);
        }

        .sticky-btn:hover {
            transform: translateY(-2px);
        }

        .sticky-btn:active {
            transform: translateY(0px);
        }

        .sticky-btn i {
            font-size: 18px;
        }

        .sticky-btn .btn-label {
            font-size: 11px;
            font-weight: 400;
            opacity: 0.7;
        }

        /* ===== АДАПТИВ ===== */
        @media (max-width: 600px) {
            body { padding: 12px; padding-bottom: 100px; }
            .glass-card { padding: 24px 16px; border-radius: 32px; }
            .hero-title { font-size: 26px; }
            .logo-text h1 { font-size: 22px; }
            .logo-icon { font-size: 34px; }
            .features { grid-template-columns: 1fr 1fr; gap: 8px; }
            .feature-item { padding: 8px 12px; }
            .feature-item span { font-size: 12px; }
            .stats { grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
            .stat-item .num { font-size: 20px; }
            .calc-row { grid-template-columns: 1fr; }
            .contacts { grid-template-columns: 1fr 1fr; }
            .sticky-bottom { padding: 12px 16px; gap: 8px; flex-wrap: wrap; }
            .sticky-btn { padding: 12px 14px; font-size: 13px; min-width: 100px; flex: 1 1 45%; }
            .promo-banner .promo-text { font-size: 13px; }
            .review-item { padding: 14px; }
        }

        @media (max-width: 400px) {
            .glass-card { padding: 18px 12px; }
            .hero-title { font-size: 22px; }
            .features { grid-template-columns: 1fr; }
            .stats { grid-template-columns: 1fr 1fr; }
            .contacts { grid-template-columns: 1fr; }
            .sticky-btn { flex: 1 1 100%; }
        }
    </style>
</head>
<body>

    <!-- ===== ЧАСТИЦЫ ===== -->
    <canvas id="particles-canvas"></canvas>

    <!-- ===== КОНТЕЙНЕР ===== -->
    <div class="container">

        <!-- ===== КАРТОЧКА 1 ===== -->
        <div class="glass-card">

            <!-- Акция -->
            <div class="promo-banner">
                <i class="fas fa-gift"></i>
                <div>
                    <div class="promo-text">🔥 АКЦИЯ: Скидка 15% на первый заказ!</div>
                    <div class="promo-desc">Действует до 01.08.2026. При заказе от 5 тонн.</div>
                </div>
            </div>

            <!-- Логотип -->
            <div class="logo-section">
                <div class="logo-icon">🚛</div>
                <div class="logo-text">
                    <h1>ПАРМА ТРАНС</h1>
                    <span>Перевозки по Пермскому краю</span>
                </div>
            </div>

            <!-- Бейдж -->
            <div class="badge"><i class="fas fa-truck-fast"></i> Работаем 24/7</div>

            <!-- Заголовок -->
            <div class="hero-title">Всё <span>ради вас</span></div>
            <div class="hero-sub">Доставим груз по Пермскому краю — от 1 кг до 20 тонн. Надёжно, вовремя, с гарантией.</div>

            <!-- Особенности -->
            <div class="features">
                <div class="feature-item">
                    <i class="fas fa-truck"></i>
                    <div>
                        <span>Фуры</span>
                        <small>до 20 т</small>
                    </div>
                </div>
                <div class="feature-item">
                    <i class="fas fa-boxes-packing"></i>
                    <div>
                        <span>Сборные</span>
                        <small>от 1 кг</small>
                    </div>
                </div>
                <div class="feature-item">
                    <i class="fas fa-temperature-low"></i>
                    <div>
                        <span>Рефрижератор</span>
                        <small>‑20°C</small>
                    </div>
                </div>
                <div class="feature-item">
                    <i class="fas fa-route"></i>
                    <div>
                        <span>Маршруты</span>
                        <small>оптимальные</small>
                    </div>
                </div>
            </div>

            <!-- Статистика -->
            <div class="stats">
                <div class="stat-item">
                    <span class="num" id="stat1">0</span>
                    <span class="label">Городов</span>
                </div>
                <div class="stat-item">
                    <span class="num" id="stat2">0</span>
                    <span class="label">Клиентов</span>
                </div>
                <div class="stat-item">
                    <span class="num" id="stat3">0%</span>
                    <span class="label">Страховка</span>
                </div>
            </div>

            <!-- Контакты -->
            <div class="contacts">
                <div class="contact-item">
                    <i class="fas fa-clock"></i>
                    <div>
                        <div class="contact-text">24/7</div>
                        <div class="contact-label">Работаем</div>
                    </div>
                </div>
                <div class="contact-item">
                    <i class="fas fa-phone"></i>
                    <div>
                        <div class="contact-text">+7 (342) 555-53-55</div>
                        <div class="contact-label">Телефон</div>
                    </div>
                </div>
            </div>

            <!-- Калькулятор -->
            <div class="calculator">
                <div class="calculator-title"><i class="fas fa-calculator"></i> Калькулятор стоимости</div>
                <div class="calc-row">
                    <input type="text" class="calc-input" id="calcFrom" placeholder="Откуда">
                    <input type="text" class="calc-input" id="calcTo" placeholder="Куда">
                </div>
                <div class="calc-row">
                    <input type="number" class="calc-input" id="calcWeight" placeholder="Вес (кг)">
                    <input type="number" class="calc-input" id="calcVolume" placeholder="Объём (м³)">
                </div>
                <div class="calc-result" id="calcResult">💰 Примерная стоимость: от 5 000 ₽</div>
            </div>

            <!-- Отзывы -->
            <div class="reviews">
                <div class="review-item">
                    <div class="review-header">
                        <div class="review-avatar">👨</div>
                        <div>
                            <div class="review-name">Алексей Иванов</div>
                            <div class="review-city">г. Пермь</div>
                        </div>
                    </div>
                    <div class="review-text">«Отличная компания! Заказывал перевозку оборудования из Перми в Березники. Всё приехало целое, даже раньше срока. Рекомендую!»</div>
                    <div class="review-stars">⭐⭐⭐⭐⭐</div>
                </div>
                <div class="review-item">
                    <div class="review-header">
                        <div class="review-avatar">👩</div>
                        <div>
                            <div class="review-name">Екатерина Смирнова</div>
                            <div class="review-city">г. Соликамск</div>
                        </div>
                    </div>
                    <div class="review-text">«Возим продукты в рефрижераторе уже 2 года. Ни разу не подвели. Водители вежливые, документы оформляют быстро.»</div>
                    <div class="review-stars">⭐⭐⭐⭐⭐</div>
                </div>
                <div class="review-item">
                    <div class="review-header">
                        <div class="review-avatar">👨</div>
                        <div>
                            <div class="review-name">Дмитрий Петров</div>
                            <div class="review-city">г. Краснокамск</div>
                        </div>
                    </div>
                    <div class="review-text">«Быстро, дёшево, надёжно. Сборный груз отправили из Краснокамска в Кунгур. Приехало за 4 часа. Супер!»</div>
                    <div class="review-stars">⭐⭐⭐⭐⭐</div>
                </div>
            </div>

            <!-- Форма -->
            <form id="orderForm">
                <div class="form-group">
                    <i class="fas fa-user"></i>
                    <input type="text" id="name" placeholder="Ваше имя" required>
                </div>
                <div class="form-group">
                    <i class="fas fa-phone"></i>
                    <input type="tel" id="phone" placeholder="Телефон" required>
                </div>
                <div class="form-group">
                    <i class="fas fa-box"></i>
                    <textarea id="message" placeholder="Описание груза (маршрут, вес, объём)"></textarea>
                </div>

                <div class="checkbox-group">
                    <input type="checkbox" id="consent" required>
                    <label for="consent">
                        Даю согласие на обработку данных по <a href="/consent" target="_blank">ФЗ-152</a>
                        <span class="required">*</span>
                    </label>
                </div>

                <button type="submit" class="submit-btn" id="submitBtn">
                    <i class="fas fa-paper-plane" style="margin-right: 12px;"></i> ОТПРАВИТЬ ЗАЯВКУ
                </button>

                <div id="status"></div>
            </form>

            <!-- Футер -->
            <div class="footer">
                <a href="/policy">Политика конфиденциальности</a>
                <span style="margin: 0 6px;">•</span>
                <a href="/consent">Согласие ФЗ-152</a>
            </div>
        </div>

    </div>

    <!-- ===== ЛИПКАЯ КНОПКА (ВНИЗУ ЭКРАНА) ===== -->
    <div class="sticky-bottom">
        <a href="tel:+73425555355" class="sticky-btn call-btn" style="text-decoration: none;">
            <i class="fas fa-phone"></i>
            <div>
                <div>Позвонить</div>
                <div class="btn-label">24/7 бесплатно</div>
            </div>
        </a>
        <a href="https://wa.me/79573453249" target="_blank" class="sticky-btn whatsapp-btn" style="text-decoration: none;">
            <i class="fab fa-whatsapp"></i>
            <div>
                <div>WhatsApp</div>
                <div class="btn-label">Написать</div>
            </div>
        </a>
    </div>

    <!-- ===== СКРИПТЫ ===== -->
    <script>
        // ===== ЧАСТИЦЫ =====
        const canvas = document.getElementById('particles-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particles = [];
        for (let i = 0; i < 60; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 2 + 1,
                speedX: (Math.random() - 0.5) * 0.5,
                speedY: (Math.random() - 0.5) * 0.5,
                opacity: Math.random() * 0.5 + 0.1
            });
        }

        function drawParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {
                p.x += p.speedX;
                p.y += p.speedY;
                if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
                if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(245, 200, 66, ${p.opacity})`;
                ctx.fill();
            });
            requestAnimationFrame(drawParticles);
        }
        drawParticles();

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        // ===== КАЛЬКУЛЯТОР =====
        function calcPrice() {
            const weight = parseInt(document.getElementById('calcWeight').value) || 0;
            const volume = parseInt(document.getElementById('calcVolume').value) || 0;
            const from = document.getElementById('calcFrom').value || '';
            const to = document.getElementById('calcTo').value || '';

            if (!from || !to || (weight === 0 && volume === 0)) {
                document.getElementById('calcResult').textContent = '💰 Заполните все поля для расчёта';
                return;
            }

            // Простая формула: 50 руб/кг + 200 руб/м³ + базовая 1000 руб
            const base = 1000;
            const weightPrice = weight * 50;
            const volumePrice = volume * 200;
            const total = base + weightPrice + volumePrice;

            document.getElementById('calcResult').textContent = `💰 Примерная стоимость: от ${total.toLocaleString()} ₽`;
        }

        document.getElementById('calcFrom').addEventListener('input', calcPrice);
        document.getElementById('calcTo').addEventListener('input', calcPrice);
        document.getElementById('calcWeight').addEventListener('input', calcPrice);
        document.getElementById('calcVolume').addEventListener('input', calcPrice);

        // ===== ОТПРАВКА ФОРМЫ =====
        document.getElementById('orderForm').onsubmit = async (e) => {
            e.preventDefault();
            const btn = document.getElementById('submitBtn');
            const status = document.getElementById('status');

            if (!document.getElementById('consent').checked) {
                status.className = 'error';
                status.textContent = '❌ Необходимо дать согласие на обработку данных';
                return;
            }

            btn.disabled = true;
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> ОТПРАВКА...';
            status.className = '';
            status.textContent = '';

            try {
                const res = await fetch('/send', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name: document.getElementById('name').value,
                        phone: document.getElementById('phone').value,
                        message: document.getElementById('message').value
                    })
                });
                const data = await res.json();
                if (data.ok) {
                    status.className = 'success';
                    status.textContent = '✅ Заявка отправлена! Мы свяжемся с вами.';
                    document.getElementById('orderForm').reset();
                } else {
                    status.className = 'error';
                    status.textContent = '❌ Ошибка отправки, попробуйте позже.';
                }
            } catch {
                status.className = 'error';
                status.textContent = '❌ Ошибка соединения. Проверьте интернет.';
            }
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane" style="margin-right: 12px;"></i> ОТПРАВИТЬ ЗАЯВКУ';
        };

        // ===== СЧЁТЧИКИ =====
        function animateCounter(el, target, suffix = '') {
            let current = 0;
            const step = Math.ceil(target / 40);
            const interval = setInterval(() => {
                current += step;
                if (current >= target) {
                    current = target;
                    clearInterval(interval);
                }
                el.textContent = current + suffix;
            }, 30);
        }

        setTimeout(() => {
            animateCounter(document.getElementById('stat1'), 30, '+');
            animateCounter(document.getElementById('stat2'), 358, '+');
            document.getElementById('stat3').textContent = '100%';
        }, 500);
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html)


# ===== ОТПРАВКА В TELEGRAM =====
@app.post("/send")
async def send(data: dict):
    text = f"""📦 НОВАЯ ЗАЯВКА

👤 Имя: {data.get('name', 'Не указано')}
📞 Телефон: {data.get('phone', 'Не указан')}
📝 Описание: {data.get('message', 'Не указано')}"""
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
        return {"ok": r.status_code == 200}
    except:
        return {"ok": False}


# ===== СТРАНИЦА СОГЛАСИЯ =====
@app.get("/consent", response_class=HTMLResponse)
async def consent():
    return HTMLResponse("""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Согласие ФЗ-152</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',Arial,sans-serif;background:#0a0f1e;padding:40px 20px;display:flex;justify-content:center;min-height:100vh}
.doc{background:rgba(255,255,255,0.04);backdrop-filter:blur(24px);padding:40px;border-radius:32px;max-width:800px;width:100%;color:#e0e8f0;border:1px solid rgba(255,255,255,0.06);box-shadow:0 30px 60px rgba(0,0,0,0.6)}
h1{color:#f5c842;border-bottom:2px solid rgba(245,200,66,0.2);padding-bottom:16px;margin-bottom:24px}
h2{color:#f5c842;margin-top:28px;margin-bottom:12px;font-size:18px}
p{line-height:1.7;margin:8px 0;color:rgba(255,255,255,0.7)}
ul{margin:8px 0 12px 24px;color:rgba(255,255,255,0.6)}
li{margin:6px 0}
.back{display:inline-block;margin-top:30px;color:#f5c842;text-decoration:none;border-bottom:1px dashed rgba(245,200,66,0.3);padding-bottom:2px;transition:0.3s}
.back:hover{border-color:#f5c842}
.light{color:rgba(255,255,255,0.3);font-size:14px}
</style>
</head>
<body>
<div class="doc">
<h1>СОГЛАСИЕ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ</h1>
<p><strong>Владелец сайта:</strong> Казанцев Максим Александрович<br>
<strong>ИНН:</strong> 595152008597<br>
<strong>Адрес:</strong> г. Пермь</p>
<p>Я, оставляя заявку на сайте <strong>ПАРМА ТРАНС</strong>, даю своё свободное, конкретное, информированное и однозначное согласие на обработку следующих персональных данных:</p>
<ul><li>Фамилия, Имя, Отчество</li><li>Контактный номер телефона</li><li>Сведения о грузе (маршрут, вес, габариты)</li></ul>
<h2>Цели обработки</h2>
<p>Связь с клиентом для уточнения деталей заказа, заключения и исполнения договора перевозки, информирования о статусе заявки.</p>
<h2>Срок хранения</h2>
<p>3 года с момента последнего обращения клиента.</p>
<h2>Отзыв согласия</h2>
<p>Путём направления письменного заявления на email: <strong>support@parmatrans159.ru</strong>. Данные будут удалены в течение 10 рабочих дней.</p>
<p class="light" style="margin-top:30px;"><em>Дата актуализации: 12.07.2026</em></p>
<a href="/" class="back">← Вернуться на главную</a>
</div>
</body>
</html>
    """)


# ===== СТРАНИЦА ПОЛИТИКИ =====
@app.get("/policy", response_class=HTMLResponse)
async def policy():
    return HTMLResponse("""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Политика конфиденциальности</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',Arial,sans-serif;background:#0a0f1e;padding:40px 20px;display:flex;justify-content:center;min-height:100vh}
.doc{background:rgba(255,255,255,0.04);backdrop-filter:blur(24px);padding:40px;border-radius:32px;max-width:800px;width:100%;color:#e0e8f0;border:1px solid rgba(255,255,255,0.06);box-shadow:0 30px 60px rgba(0,0,0,0.6)}
h1{color:#f5c842;border-bottom:2px solid rgba(245,200,66,0.2);padding-bottom:16px;margin-bottom:24px}
h2{color:#f5c842;margin-top:28px;margin-bottom:12px;font-size:18px}
p{line-height:1.7;margin:8px 0;color:rgba(255,255,255,0.7)}
ul{margin:8px 0 12px 24px;color:rgba(255,255,255,0.6)}
li{margin:6px 0}
.back{display:inline-block;margin-top:30px;color:#f5c842;text-decoration:none;border-bottom:1px dashed rgba(245,200,66,0.3);padding-bottom:2px;transition:0.3s}
.back:hover{border-color:#f5c842}
.light{color:rgba(255,255,255,0.3);font-size:14px}
</style>
</head>
<body>
<div class="doc">
<h1>ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ</h1>
<p><strong>Владелец сайта:</strong> Казанцев Максим Александрович (ИНН 595152008597)<br>
<strong>Контактный email:</strong> support@parmatrans159.ru</p>
<h2>1. Общие положения</h2>
<p>Настоящая Политика определяет порядок обработки и защиты персональных данных пользователей сайта <strong>ПАРМА ТРАНС</strong>.</p>
<h2>2. Какие данные собираются</h2>
<ul><li>Фамилия, Имя, Отчество</li><li>Контактный номер телефона</li><li>Информация о грузе (маршрут, вес, габариты)</li><li>IP-адрес, тип браузера, время посещения (для технической безопасности)</li></ul>
<h2>3. Цели сбора</h2>
<ul><li>Обработка заявок на грузоперевозку</li><li>Заключение и исполнение договоров перевозки</li><li>Информирование о статусе заказа</li><li>Улучшение качества обслуживания</li></ul>
<h2>4. Передача третьим лицам</h2>
<p>Персональные данные не передаются третьим лицам, за исключением случаев, прямо предусмотренных законодательством Российской Федерации.</p>
<h2>5. Права пользователя</h2>
<p>Вы имеете право: отозвать согласие на обработку данных, запросить копию своих данных, потребовать удаления или уточнения данных.</p>
<p>Для этого направьте обращение на email: <strong>support@parmatrans159.ru</strong>.</p>
<p class="light" style="margin-top:30px;"><em>Дата актуализации: 12.07.2026</em></p>
<a href="/" class="back">← Вернуться на главную</a>
</div>
</body>
</html>
    """)
