import telepot
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

api_token = os.getenv('API_TOKEN')

TelegramBot = telepot.Bot(api_token)
print(TelegramBot.getMe()) #it gives you metadata

print(TelegramBot.getUpdates()) #it gives you updates of your bot

# In console you got update ID you can use it for your new updates.

# Access the API token
