import os.path
from datetime import datetime
from db.repositories.locales import LocalesRepository
from db.schema import Schema
from crosscutting.helpers import get_json_dict, dump_to_file, open_from_file
from sqlalchemy import insert
from skyscanner_service.skyscanner_service import get_flights_synced, get_dataset

def initialize_schema():
    schema = Schema()
    schema.reset_schema()

    currencies_dictionary = get_dataset_dictionary('currencies')
    insert_currencies(currencies_dictionary['currencies'])

    locales_dictionary = get_dataset_dictionary('locales')
    insert_locales(locales_dictionary['locales'])

    markets_dictionary = get_dataset_dictionary('markets')
    insert_markets(markets_dictionary['markets'])

def get_dataset_dictionary(dataset_name):
    dataset_path = 'crosscutting/datasets/'+dataset_name+'.json'
    dataset_dictionary = {}

    if os.path.isfile(dataset_path):
        dataset_dictionary = open_from_file(dataset_path)
    else:
        data_source = get_dataset(dataset_name)
        dataset_dictionary = get_json_dict(data_source)
        dump_to_file('dumps/locales.json', dataset_dictionary)

    return dataset_dictionary

def insert_itineraries(flights):
    # TODO: replace this time with the time the query was executed
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")

    schema = Schema()
    with schema.create_transaction() as tx:
        table = tx.schema.tables['itineraries']
    
        for key, value in flights.items():
            # TODO: Ugly code to be improved one business rules are clearer (likely with joint tables)
            pricingOptions = value['pricingOptions'][0]
            items = pricingOptions['items'][0]
            flight_dto = {
                'timestamp': timestamp,
                'itineraryId': key,
                'price': items['price']['amount'],
                'link': items['deepLink']
            }
            query = insert(table).values(flight_dto)
            tx.conn.execute(query)
    
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
