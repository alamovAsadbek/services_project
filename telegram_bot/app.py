import os
import re

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from dotenv import load_dotenv

from keyboards import keyboards

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Warning
@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.VOICE,
                                   types.ContentType.DOCUMENT, types.ContentType.LOCATION, types.ContentType.AUDIO])
async def handle_check_message(message: types.Message):
    await message.reply("Botga faqat matnli xabar yuboring! 📝", reply_markup=keyboards.main_keyboards)


# end warning


# @dp.message_handler(lambda message: message.chat.id != int(ADMIN_ID), state=None)
# async def admin_reply(message: types.Message):
#     await dp.current_state(user=message.from_user.id).set_state('get_message')
#

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f"<b>Assalom Aleykum {message.from_user.full_name}! 👋  Botga xush kelibsiz !!! 🤖</b>",
                        reply_markup=keyboards.main_keyboards)


@dp.message_handler(text="Xabar Yuborish ✍️", state=None)
async def send_message_button(message: types.Message):
    await message.reply("Xabarni kiriting 👇:", reply_markup=keyboards.main_keyboards)
    await dp.current_state(user=message.from_user.id).set_state('get_message')


@dp.message_handler(state='get_message', content_types=types.ContentTypes.TEXT)
async def get_message(message: types.Message, state: FSMContext):
    text = message.text
    user_id = ADMIN_ID
    await bot.send_message(
        chat_id=user_id,
        text=f"Sizga yangi xabar mavjud ✍️ : \n\n{text} \n\nUsername: {message.from_user.username}\n"
             f"User ID: {message.from_user.id} \nFull Name: {message.from_user.full_name}",
        reply_markup=keyboards.main_keyboards
    )
    await message.reply("Sizning xabaringiz yuborildi! ✅", reply_markup=keyboards.main_keyboards)
    await state.update_data(user_id=message.from_user.id)
    await state.finish()


@dp.message_handler(text=["Bog'lanish ☎️"])
async def help_command(message: types.Message):
    text = f'''
        <b>A'lamov Asadbek bilan bog'lanish uchun manzillar: </b>

<a href="https://t.me/alamov_asadbek">Telegram 🌐</a>

<a href="https://instagram.com/alamov_asadbek">Instagram 🌐</a>

<a href="https://www.linkedin.com/in/alamov-asadbek/">LinkedIn 🌐</a>

<a href="https://www.facebook.com/alamov.asadbek/">Facebook 🌐</a>

<a href="https://x.com/alamov_asadbek">X 🌐</a>

<a href="tel:{os.getenv('PHONE_NUMBER')}">{os.getenv('PHONE_NUMBER')} ☎️</a>

    '''
    await message.reply(text, parse_mode=types.ParseMode.HTML)


def split_message(message: str):
    result = {}
    user_id = re.search(r"User ID: (\d+)", message)
    if user_id:
        result["user_id"] = user_id.group(1)
    return result


# reply for admin
@dp.message_handler(lambda message: message.chat.id == int(ADMIN_ID), state=None)
async def admin_reply(message: types.Message):
    reply_message = message['reply_to_message']['text']
    result_data = split_message(reply_message)
    user_id = result_data['user_id']
    if user_id:
        await bot.send_message(user_id,
                               f"Sizga <b>A'lamov Asadbekdan </b> yangi xabar bor✍️: \n\n{message.text}",
                               reply_markup=keyboards.main_keyboards)
        await message.reply("Javob foydalanuvchiga yuborildi! ✅", reply_markup=keyboards.main_keyboards)
    else:
        await message.reply("Foydalanuvchidan kelgan xabarni topa olmadim. Xabar yuborish uchun xabarni belgilang! 😬")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
