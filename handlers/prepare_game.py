from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from states.game import Game

router = Router()
prepare_text = 'Вы зашли в соседнюю комнату, сели за стол, и вам предложили ввести имя. Какое оно будет?'


@router.callback_query(F.data == 'prepare', StateFilter(None))
async def prepare_callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(prepare_text)
    await state.set_state(Game.name)


@router.message(StateFilter(Game.name))
async def set_name(message: types.Message, state: FSMContext):
    if message.text.upper not in ['GOD', 'DEALER', 'SINORTAX'] and len(message.text) <= 6:
        await message.reply('Удачи')
        await state.update_data(name=message.text.upper())
        await state.set_state(Game.game)
    elif len(message.text) > 6:
        await message.reply('Максимальная длина имени 6 символов')
    else:
        await message.answer('Данное имя занято')
