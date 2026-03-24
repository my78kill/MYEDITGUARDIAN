import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID"))
SUDO_ID = list(map(int, os.environ.get("SUDO_ID", "").split()))
MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DB_NAME")
LOGGER = os.environ.get("LOGGER", "True") == "True"
BOT_NAME = os.environ.get("BOT_NAME", "Edit Guardian")
SUPPORT_ID = int(os.environ.get("SUPPORT_ID"))
