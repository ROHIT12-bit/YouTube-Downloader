import os
import time
import threading
from flask import Flask

from pyrogram import Client, idle
from pyrogram.errors import FloodWait
from config import Config

# =========================
# Pyrogram Bot
# =========================
bot = Client(
    "bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=50,
    plugins=dict(root="plugins")
)

def run_bot():
    while True:
        try:
            bot.start()
            print("🤖 Bot Started Successfully")
            idle()          # keep bot alive
            bot.stop()
            break
        except FloodWait as e:
            wait = int(getattr(e, "value", 60))
            print(f"⏳ FloodWait detected. Sleeping {wait}s...")
            time.sleep(wait + 2)
        except Exception as e:
            print(f"❌ Bot crashed: {e}")
            time.sleep(5)

# =========================
# Flask Keep-Alive Server
# =========================
web = Flask(__name__)

@web.route("/")
def home():
    return "✅ BotsKingdoms Bot is alive"

def run_web():
    port = int(os.environ.get("PORT", "10000"))
    web.run(host="0.0.0.0", port=port)

# =========================
# Main
# =========================
if __name__ == "__main__":
    # Start Flask in background (Render needs a port)
    threading.Thread(target=run_web, daemon=True).start()

    # Start Telegram bot (polling)
    run_bot()    web.run(host="0.0.0.0", port=port)

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    # Start Flask in background
    threading.Thread(target=run_web, daemon=True).start()

    # Start Telegram bot
    run_bot()
