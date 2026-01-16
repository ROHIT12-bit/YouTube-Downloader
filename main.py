import os
import threading
from flask import Flask

from pyrogram import Client, idle
from config import Config

# -------------------------
# Pyrogram Bot
# -------------------------
bot = Client(
    "bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=50,
    plugins=dict(root="plugins")
)

def run_bot():
    bot.start()
    print("🤖 Bot Started Successfully")
    idle()          # keeps bot running
    bot.stop()

# -------------------------
# Flask Keep-Alive Server
# -------------------------
web = Flask(__name__)

@web.get("/")
def home():
    return "✅ Bot is alive"

def run_web():
    port = int(os.environ.get("PORT", "10000"))
    web.run(host="0.0.0.0", port=port)

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    # Start Flask in background
    threading.Thread(target=run_web, daemon=True).start()

    # Start Telegram bot
    run_bot()
