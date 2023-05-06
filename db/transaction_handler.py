from db.repositories.locales import LocalesRepository
from db.schema import Schema
from crosscutting.helpers import get_json_dict, dump_to_file
from sqlalchemy import insert
from skyscanner_service.skyscanner_service import get_flights_synced, get_locales, get_markets, get_currencies

def initialize_schema():
    schema = Schema()
    schema.reset_schema()

    currencies = get_currencies()
    currencies_dictionary = get_json_dict(currencies)
    insert_currencies(currencies_dictionary['currencies'])

    locales = get_locales()
    locales_dictionary = get_json_dict(locales)
    # dump_to_file('dumps/locales.json', locales_dictionary)
    insert_locales(locales_dictionary['locales'])

    markets = get_markets()
    markets_dictionary = get_json_dict(markets)
    insert_markets(markets_dictionary['markets'])


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
