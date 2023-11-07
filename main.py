import asyncio, logging, sys, os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import start, add_data, get_data, out_of_flow

TOKEN = os.getenv('add_get_data_bot_token')

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def main() -> None:
    """Main function: starts polling updates using start command, add data and get data routers"""

    dp.include_routers(start.router, add_data.router, get_data.router, out_of_flow.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
