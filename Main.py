import os
import time
import threading
import requests
from flask import Flask
from datetime import datetime

# Flask App - Render ko zinda rakhne ke liye
app = Flask(__name__)

@app.route('/')
def home():
    return "ALI PRO TRADER 10-BOT ORIGINAL ACCURACY IS LIVE! 🚀"

# ================= CONFIG =================
BOT_TOKEN = os.environ.get("BOT_TOKEN") 
CHAT_ID = os.environ.get("CHAT_ID")

def send_signal(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("ERROR: BOT_TOKEN ya CHAT_ID nahi mila! Env me set karo!")
        return
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, data=data)
        print(f"Signal Sent: {message[:50]}")
    except Exception as e:
        print(f"Send Error: {e}")

# ============== 10-BOT LOGIC ==============
# Yahan aapka original accuracy wala logic hai
def check_market_and_generate_signal():
    # Ye dummy logic hai - Yahan aap apna 10 indicator wala original code lagao
    # Main yahan structure de raha hu
    
    # Example: Har 5 min me ek signal
    # Aapka original logic yahan se start hoga
    now = datetime.now().strftime("%H:%M:%S")
    
    # --- APNA ORIGINAL 10-BOT LOGIC YAHAN PASTE KARO ---
    # For example:
    # if RSI + MACD + EMA etc... condition true:
    #   return "📈 BUY SIGNAL - BTCUSDT..."
    # else:
    #   return None
    
    # Demo signal for testing (Is line ko baad me hata dena)
    return f"✅ *ALI PRO TRADER TEST SIGNAL*\nTime: {now}\nPair: BTCUSDT\nAction: BUY (Original Accuracy)\nStatus: Bot Working Perfect!"

def bot_loop():
    print("10-BOT Loop Started...")
    send_signal("🚀 *ALI PRO TRADER 10-BOT ONLINE*\nOriginal Accuracy Bot Started on Render!")
    while True:
        try:
            signal = check_market_and_generate_signal()
            if signal:
                send_signal(signal)
            # Har 5 minute me check karega - Aap 60 ya 300 kar sakte ho
            time.sleep(300) 
        except Exception as e:
            print(f"Bot Loop Error: {e}")
            time.sleep(30)

# ============== START BOTH ==============
# Ye sabse important fix hai!
threading.Thread(target=bot_loop, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
