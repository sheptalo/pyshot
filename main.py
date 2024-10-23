import asyncio
from props import bot, dp

from handlers.start import router as start_router
from handlers.prepare_game import router as prepare_game_router
from handlers.game import router as game_router


async def main():
    dp.include_routers(start_router, prepare_game_router, game_router)
    await dp.start_polling(bot)


asyncio.run(main())
