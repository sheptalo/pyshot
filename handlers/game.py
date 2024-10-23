from aiogram import types, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from states.game import Game

router = Router()


@router.callback_query(StateFilter(Game.game))
async def handle_game(call: types.CallbackQuery):
    pass
