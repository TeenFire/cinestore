import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6094762122:AAFMjkALs6_fKABW15GsEheB_rqPidRzwrQ")
APP_ID = int(os.environ.get("APP_ID", "1736204"))
API_HASH = os.environ.get("API_HASH", "890d40e0f91a4de32dec2965444b2cbe")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001205507869"))
OWNER_ID = int(os.environ.get("OWNER_ID", "1058015838"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://cinestore:cinestore@cinestore.gxqbify.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "FileStore")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "<b><i>💐 Hello {first}, \n\n⛵ I'm Just A File-Store Bot Specially Made To Store Telegram Files</i></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1058015838").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>You Can't Send Me Your Posts Directly❗️</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1058015838)

LOG_FILE_NAME = "File-Store.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
