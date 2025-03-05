from pyrogram import Client
from pyrogram.types import Message
from mistralai import Mistral
from mistralai.models.sdkerror import SDKError

from settings import (
    BOT_TOKEN, API_ID, API_HASH, MISTRAL_TOKEN
)
from utils import gpt_4o_response

bot = Client('bot', bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)
client = Mistral(api_key=MISTRAL_TOKEN)


@bot.on_message()
async def echo(_, message: Message):
    try:
        temp_message = await bot.send_message(chat_id=message.chat.id, text='думаю...')
        response = gpt_4o_response(client, message.text)
        await bot.edit_message_text(
            chat_id=temp_message.chat.id,
            message_id=temp_message.id,
            text=response
        )
    except AttributeError:
        pass
    except SDKError:
        await bot.send_message(chat_id=message.chat.id, text='Лимит запросов за час')

while True:
    print('Запущен')
    bot.run()
