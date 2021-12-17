import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor 
import csv, datetime, pymysql

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Привет")
    statictics(message.chat.id, message.text)
    stat(message.chat.id, message.text)

def statictics(user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([data, user_id, command])

def stat(user_id, command):
    connection = pymysql.Connect(host='', port=3306, user='', passwd='', db='')
    cursor = connection.cursor()
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES ('%s', '%s', '%s')" % (user_id, command, data))
    connection.commit()
    cursor.close()

if __name__ == '__main__':
    executor.start_polling(dp)