from aiogram.fsm.state import StatesGroup, State


class Game(StatesGroup):
    name = State()
    confirm_name = State()
    game = State()
