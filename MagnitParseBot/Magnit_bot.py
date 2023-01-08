from main import collect_data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiofiles import os
import sqlite3


API_Token = "5799249055:AAERdPZxJw7X1ueEwMu821lN3QZ4P5yyWlk"

bot = Bot(token=API_Token)

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):

    start_buttons = ['Moscow', 'Ekaterinburg', 'Saint-Peterburg', 'Chelyabinsk', 'Novosibirsk', 'Krasnodar']

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    connect = sqlite3.connect('users.db')

    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")

    connect.commit()

    people_id = message.chat.id

    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")

    data = cursor.fetchone()

    print(data)

    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()

    else:
        message.answer(message.chat.id, 'Such a user already exists')

    await message.answer('Please select a City', reply_markup=keyboard)


@dp.message_handler(Text(equals='Moscow'))
async def moscow_city(message: types.Message):

    await message.answer('Please waiting...')

    chat_id = message.chat.id

    await send_data(city_code='2398', chat_id=chat_id)


@dp.message_handler(Text(equals='Ekaterinburg'))
async def ekb_city(message: types.Message):

    await message.answer('Please waiting...')

    chat_id = message.chat.id

    await send_data(city_code='1869', chat_id=chat_id)


@dp.message_handler(Text(equals='Saint-Peterburg'))
async def ekb_city(message: types.Message):

    await message.answer('Please waiting...')

    chat_id = message.chat.id

    await send_data(city_code='1645', chat_id=chat_id)


@dp.message_handler(Text(equals='Chelyabinsk'))
async def ekb_city(message: types.Message):

    await message.answer('Please waiting...')

    chat_id = message.chat.id

    await send_data(city_code='2001', chat_id=chat_id)


@dp.message_handler(Text(equals='Novosibirsk'))
async def ekb_city(message: types.Message):

    await message.answer('Please waiting...')

    chat_id = message.chat.id

    await send_data(city_code='2425', chat_id=chat_id)


@dp.message_handler(Text(equals='Krasnodar'))
async def ekb_city(message: types.Message):

    await message.answer('Please waiting...')

    chat_id = message.chat.id

    await send_data(city_code='1761', chat_id=chat_id)


async def send_data(city_code='', chat_id=''):

    file = await collect_data(city_code=city_code)

    await bot.send_document(chat_id=chat_id, document=open(file, 'rb'))

    await os.remove(file)


if __name__ == '__main__':
    executor.start_polling(dp)