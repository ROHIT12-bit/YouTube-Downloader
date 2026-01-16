import os
import threading
from flask import Flask

# --- Flask keep-alive ---
web = Flask(__name__)

@web.get("/")
def home():
    return "OK"

def run_web():
    port = int(os.environ.get("PORT", "10000"))
    web.run(host="0.0.0.0", port=port)

# --- start both ---
if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    app.run()   # <-- keep your existing Pyrogram Client variable name here
