from sqlalchemy import (create_engine, Boolean, Column, ForeignKey, Integer, MetaData, String, Table)
from config import conn_string

class Schema:
    def __init__(self):
        self.engine = create_engine(conn_string, echo=True, future=True)
        self.metadata = MetaData()
        self.tables = self.__generate_tables()

    def create_all_tables(self):
        self.metadata.create_all(self.engine)
    
    def drop_all_tables(self):
        self.metadata.drop_all(self.engine)

    # Crea el contexto para ejecutar transacciones. Se utiliza cada vez que ejecutamos transacciones.
    # Usarlo con el 'with', asi al terminar el bloque se ejecuta el metodo __exit__ y commitea
    def create_transaction(self):
        return TransactionManager(self)
    
    def __generate_tables(self):
        return {
            'todo': Table(
                'todo',
                self.metadata,
                Column('id', Integer, primary_key=True, autoincrement=True ),
                Column('user_id', Integer, ForeignKey('user.id')),
                Column('description', String(500)),
                Column('active', Boolean)
            ),
            'user': Table(
                'user',
                self.metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('email', String(50)),
                Column('fullname', String(50))
            ),
            'locales': Table(
                'locales',
                self.metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('code', String(10)),
                Column('name', String(250))
            ),
            'markets': Table(
                'markets',
                self.metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('code', String(2)),
                Column('name', String(150)),
                Column('currency', String(3))
            ),
            'currencies': Table(
                'currencies',
                self.metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('code', String(3)),
                Column('symbol', String(10)),
                Column('thousandsSeparator', String(10)),
                Column('decimalSeparator', String(10)),
                Column('symbolOnLeft', Boolean),
                Column('spaceBetweenAmountAndSymbol', Boolean),
                Column('decimalDigits', Integer),
            )
        }

class TransactionManager:
    def __init__(self, schema):
        self.schema = schema
        self.conn = self.schema.engine.connect()
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()