from dotenv import load_dotenv
import os

load_dotenv(encoding='utf-8')
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_TOKEN = os.getenv('API_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SYSTEM = 'You are an AI assistant who knows everything.'
MISTRAL_TOKEN = os.getenv('MISTRAL_TOKEN')
