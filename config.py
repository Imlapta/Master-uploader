import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7948276603:AAGOOpHsQcPZ3ILpw5BX9GuwBbAGrvEGjX8")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "3737117"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "f466ca6ff400954d192ce0992ddf8b5d")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "1110590703").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
