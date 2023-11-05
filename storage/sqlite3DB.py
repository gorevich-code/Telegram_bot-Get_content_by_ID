import sqlite3
from sqlite3 import Error
from typing import Union

class SQLiteDB:
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.table_name = None
        self.table_columns = None

    def create_connection(self):
        """Creates connection to DB"""
        connection = None
        database_path_name = f"./{self.db_name}.db"
        try:
            connection = sqlite3.connect(database_path_name)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def execute_query(self, query: str):
        """Executes query to DB"""
        connection = self.create_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            last_inserted_id = cursor.fetchone()
            connection.commit()
            print(f"Query executed successfully")

        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if (connection):
                connection.close()
                print("SQL connection closed")
            return last_inserted_id

    def create_table(self, table_name, table_columns):
        self.table_name = table_name
        self.table_columns = table_columns
        table_columns = ', '.join(self.table_columns)
        query = f"CREATE TABLE if not exists {self.table_name}({table_columns});"
        self.execute_query(query)

    def _get_formatted_table_columns_data(self) -> str:
        """ Helper method which converts raw table columns data to string with columns names with comma between except autofill 'id' column"""

        return ", ".join(
            tuple(x.split(' ')[0] for x in self.table_columns[1::])
        )

    def insert_data(self, data):
        """Method to insert data into DB"""

        table_columns = self._get_formatted_table_columns_data()

        query = f"""
        INSERT INTO {self.table_name} ({table_columns})
        VALUES ({data})
        RETURNING id;
        """
        last_inserted_id = self.execute_query(query)[0]
        return last_inserted_id
    
    def get_data_by_id(self, data_id: Union[int, str]):
        """Method to get data fromo DB by ID"""
        table_columns = self._get_formatted_table_columns_data()
        query = f"""
        SELECT {table_columns} FROM {self.table_name} 
        WHERE id='{data_id}'
        """
        recieved_data = self.execute_query(query)
        return recieved_data
    
db = SQLiteDB(db_name='BotStorage')
db.create_table(
    table_name='Storage',
    table_columns=('id INTEGER UNIQUE PRIMARY KEY', 'message_chat BLOB', 'message_id INTEGER', 'message_date NUMERIC')
)
