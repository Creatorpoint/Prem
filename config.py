# ============================================================
# Group Manager Bot
# Support: https://t.me/primexprem
# Channel: https://t.me/primexprem
# YouTube: https://t.me/primexprem
# License: Open-source (keep credits, no resale)
# ============================================================

import os
from dotenv import load_dotenv

load_dotenv()

# Required configurations
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

OWNER_ID = int(os.getenv("OWNER_ID", 0))
BOT_USERNAME = os.getenv("BOT_USERNAME", "NomadeHelpBot")

SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/PRIME_X_CHAT2")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/primexprem")
START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/rfsmvd.jpg")
