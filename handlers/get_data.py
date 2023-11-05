from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data_models.user_message_data_model import BasicMessageDataModel
from aiogram.utils.markdown import hbold
from storage.sqlite3DB import db as SQLite3_DB
import main


router = Router()

class DataToGive(StatesGroup):
    get_data_from_db = State()

@router.message(Command('get'))
async def command_add_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/get` command
    """
    await message.answer(f"I`m ready to send data from my storage. Message me the data ID"
                         f"\n\nCall /get_cancel to abort {hbold('get')} flow")
    await state.set_state(DataToGive.get_data_from_db)


@router.message(Command('get_cancel'), DataToGive.get_data_from_db)
async def command_get_cancel_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/add` command
    """
    await state.clear()
    await message.answer(f"Get data flow canceled")



@router.message(DataToGive.get_data_from_db)
async def recieve_data(message: Message, state: FSMContext):
    """
    This handler receives ID from the next message after `/get` command and return message
    with specified ID from DB if exists

    """
    if not message.text.isdigit():
        await message.answer('Invalid ID format. Digits only. Please try again :)')
        return
    data_from_storage = BasicMessageDataModel.read_from_db(db=SQLite3_DB, data_id=message.text)
    if data_from_storage:
        await data_from_storage.copy_to(chat_id=message.chat.id).as_(main.bot)
    else:
        await message.answer('No data saved under this ID')
    await state.clear()
