# ============================================================
# Group Manager Bot
# Support: https://t.me/primexprem
# Channel: https://t.me/primexprem
# YouTube: https://t.me/primexprem
# License: Open-source (keep credits, no resale)
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    print("✅ Group commands registered!")
