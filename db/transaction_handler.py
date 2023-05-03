from db.repositories.locales import LocalesRepository
from db.schema import Schema
from sqlalchemy import insert

def reset_schema():
    schema = Schema()
    schema.drop_all_tables()
    schema.create_all_tables()

def insert_locales(locales):
    schema = Schema()
    with schema.create_transaction() as tx:
        table = tx.schema.tables['locales']

        for local in locales:
            local_dto = {
                'code': local['code'],
                'name': local['name']
            }
            query = insert(table).values(local_dto)
            tx.conn.execute(query)
        locales = LocalesRepository(tx).find_all()
        print(locales.fetchall())

def insert_markets(markets):
    schema = Schema()
    with schema.create_transaction() as tx:
        table = tx.schema.tables['markets']

        for market in markets:
            market_dto = {
                'code': market['code'],
                'name': market['name'],
                'currency': market['currency']
            }
            query = insert(table).values(market_dto)
            tx.conn.execute(query)
        locales = LocalesRepository(tx).find_all()
        print(locales.fetchall())

def insert_currencies(currencies):
    schema = Schema()
    with schema.create_transaction() as tx:
        table = tx.schema.tables['currencies']

        for currency in currencies:
            currency_dto = {
                'code': currency['code'],
                'symbol': currency['symbol'],
                'thousandsSeparator': currency['thousandsSeparator'],
                'decimalSeparator': currency['decimalSeparator'],
                'symbolOnLeft': currency['symbolOnLeft'],
                'spaceBetweenAmountAndSymbol': currency['spaceBetweenAmountAndSymbol'],
                'decimalDigits': currency['decimalDigits']
            }
            query = insert(table).values(currency_dto)
            tx.conn.execute(query)
        locales = LocalesRepository(tx).find_all()
        print(locales.fetchall())
