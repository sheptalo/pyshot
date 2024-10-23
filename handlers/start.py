from aiogram import Router, types
from aiogram.filters import CommandStart, StateFilter
from keyboards.menu import *

router = Router()


@router.message(CommandStart(), StateFilter(None))
async def start_handler(message: types.Message):
    await message.reply(f'Привет {message.from_user.first_name}! Ты очнулся в ванной клуба',
                        reply_markup=menu_markup)
