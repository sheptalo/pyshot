from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
load_dotenv()

bot = Bot(os.environ["BOT_TOKEN"])
dp = Dispatcher()
