# ============================================================
# Group Manager Bot
# Support: https://t.me/primexprem
# Channel: https://t.me/primexprem
# YouTube: https://t.me/primexprem
# License: Open-source (keep credits, no resale)
# ============================================================

import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "group_manager_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from handlers import register_all_handlers
register_all_handlers(app)

print("✅ Bot is starting securely...")

app.run()
