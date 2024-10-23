from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


_kb = [
    [InlineKeyboardButton(text='Выйти из ванной', callback_data='prepare')],
]

menu_markup = InlineKeyboardMarkup(inline_keyboard=_kb)

__all__ = ['menu_markup']
