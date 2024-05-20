from aiogram import Bot, Dispatcher,types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command = '/start', description = "say hi to this fella"),
        types.BotCommand(command = '/help', description="ask for assistance"),
        types.BotCommand(command='/lobotomy', description="but would you win?")
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands = 'start')
async def start(message: types.Message):
    await message.reply('hiiiiii')

@dp.message_handler(commands = 'help')
async def help(message: types.Message):
    await message.reply('how about you kindly discombobulat e')

@dp.message_handler(commands='lobotomy')
async def help(message: types.Message):
    await message.reply('am i the worst telegram bot because i was made by you, or was i made by you because i am the worst telegram bot?')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('a very thoughtful reply, hm yes yes i agree')

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)