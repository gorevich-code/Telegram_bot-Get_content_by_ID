from aiogram.types import Message
import sqlite3


class BasicMessageDataModel:
    """
    Class which represents message data model which contains data required to copy message
    """
    def __init__(self, message: Message) -> None:
        self.message_chat = f'{message.chat.model_dump()}'
        self.message_id = message.message_id
        self.message_date=message.date
    
    def write_to_db(self, db:sqlite3) -> str:
        """Write message data to DB"""
        data_to_insert = f'"{self.message_chat}", "{self.message_id}", "{self.message_date}"'
        record_id = db.insert_data(data_to_insert)
        return record_id
    
    def convert_str_to_dict(input_string: str)-> dict:
        """Converts message chat model dump from string to dictionary"""
        output_dict = {}
        for elem in input_string[1:-1].split(','):
            key,value = elem.split(':')
            key = key.replace(' ', '').replace("'", '')
            value = value.replace(' ', '').replace("'", '')
            value = int(value) if value.isdigit() else value
            value = None if 'None' in str(value) else value
            output_dict[key] = value
        return output_dict
    
    @classmethod
    def read_from_db(cls, db:sqlite3, data_id):
        """Read message data from DB by ID
        
        :return: message: Message if data found by specified ID else None
        """
        data_from_db = db.get_data_by_id(data_id)
        if data_from_db:
            chat, id, date = data_from_db
        else:
            return None
        chat = cls.convert_str_to_dict(chat)
        return Message(chat=chat, message_id=id, date=date)
