from abc import ABC, abstractmethod
from sqlalchemy import insert, select, update 
from sqlalchemy.exc import InvalidRequestError

class BaseRepository(ABC):
    def __init__(self, tx):
        self.conn = tx.conn
        self.schema = tx.schema
    
    def find_all(self):
        query = select(self._get_table())
        return self.conn.execute(query)
    
    def find_by_id(self, id):
        table = self._get_table()
        query = select(table).where(table.c.id == id)
        response = self.conn.execute(query)
        if response:
            return response.fetchone()
        
    def insert(self, user):
        table = self._get_table()
        query = insert(table).values(user)
        response = self.conn.execute(query)
        return response.inserted_primary_key[0]

    def update(self, user):
        prev_user = self.find_by_id(user['id'])
        if not prev_user:
            raise InvalidRequestError('Invalid id')
        query = update(self._get_table).values(user)
        self.conn.execute(query)

    @abstractmethod
    def _get_table(self):
        pass