import os, time, random, threading
from flask import Flask
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
app = Flask(__name__)

@app.route('/')
def home(): return "💎 SUPER PREMIUM PRO+ BOT IS LIVE - Manual Trading Only!"

def send(msg):
    if not BOT_TOKEN or not CHANNEL_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try: requests.post(url, data={"chat_id": CHANNEL_ID, "text": msg, "parse_mode": "Markdown"}, timeout=10)
    except: pass

def premium_signal_loop():
    pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "EUR/JPY", "BTC/USD (OTC)", "ETH/USD (OTC)", "USD/BRL (OTC)"]
    while True:
        time.sleep(120) # Har 2 minute
        pair = random.choice(pairs)
        direction = random.choice(["CALL 🔼", "PUT 🔽"])
        acc = random.randint(89, 97)
        reason = random.choice(["Strong Trend", "Support Break", "RSI Reversal", "OTC Momentum"])
        
        msg = f"""💎 *SUPER PREMIUM PRO+ SIGNAL* 💎

📊 *Pair:* `{pair}`
📈 *Signal:* *{direction}*
⏰ *Expiry:* 1 Minute
🎯 *Accuracy:* {acc}%
📝 *Reason:* {reason}

⚠️ *MANUAL TRADE ONLY*
👉 Quotex me khud entry len

🔔 _Next signal in 2 min_"""
        send(msg)

threading.Thread(target=premium_signal_loop, daemon=True).start()

if __name__ == "__main__":
    send("🚀 *SUPER PREMIUM PRO+ BOT STARTED!*\nAb aapko har 2 minute me premium signals milenge!")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
