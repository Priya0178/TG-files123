import os

API_ID = int(os.environ.get("API_ID", "19397648"))
API_HASH = os.environ.get("API_HASH", "ed2db4aa6ab5f67fde7b88b8f17e85d0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5464339478:AAExMDU2ChelgnqW0P2WsuVxlWe6JBo76iY")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001773229209")
IS_PRIVATE = os.environ.get("IS_PRIVATE", True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "1092802988"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "1092802988").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
