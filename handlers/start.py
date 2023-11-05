from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold


router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! " +
                         "\n\nI am BOT which can save your data - text, photo, geo." +
                         "\nThe next commands are available: \n\n/add - to add data \n/get - get data")
