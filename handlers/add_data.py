from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data_models.user_message_data_model import BasicMessageDataModel
from storage.sqlite3DB import db as SQLite3_DB


router = Router()


class DataToSave(StatesGroup):
    new_data_input = State()


@router.message(Command('add'))
async def command_add_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/add` command
    """
    await message.answer(
        f"I`m ready to remember. Message me some text or attachment" +
        f"\n\nCall /add_cancel to abort {hbold('add')} flow"
        )
    await state.set_state(DataToSave.new_data_input)

@router.message(Command('add_cancel'), DataToSave.new_data_input)
async def command_add_cancel_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/add` command
    """
    await state.clear()
    await message.answer(f"Add data flow canceled")

@router.message(DataToSave.new_data_input)
async def recieve_data(message: Message, state: FSMContext):
    """
    This handler receives message the next message after `/add` command and save message data to DB
    """
    data = BasicMessageDataModel(message=message)
    record_id = data.write_to_db(db=SQLite3_DB)
    await message.answer(f"Your record successfully saved. Record id: {hbold(record_id)}")
    await state.clear()
