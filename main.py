# ============================================================
# Group Manager Bot + Web Dashboard
# ============================================================

import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
from handlers import register_all_handlers
import threading
import web
import os

logging.basicConfig(level=logging.INFO)

app = Client(
    "group_manger_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_all_handlers(app)

# ============================================================
# RUN WEB SERVER
# ============================================================
def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

# ============================================================
# START BOT
# ============================================================
print("🚀 Bot + Web starting...")
app.run()
