from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message()
async def out_of_flow_handler(message: Message) -> None:
    """
    This handler receives messages which send out of start / add / get command flow
    """
    await message.answer("Out of command message. Please call any command firstly and then message me or attach any :)" +
                         "\nThe next commands are available: \n\n/add - to add data \n/get - get data")
