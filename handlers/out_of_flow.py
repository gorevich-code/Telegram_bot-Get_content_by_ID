from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.methods.send_message import SendMessage
from aiogram.methods import ForwardMessage


router = Router()

@router.message()
async def out_of_flow_handler(message: Message) -> None:
    """
    This handler receives messages which send out of start / add / get command flow
    """
    await message.answer(f"Out of command message. Please call any command firstly and then message me or attach any :)" +
                         "\nThe next commands are available: \n\n/add - to add data \n/get - get data")
