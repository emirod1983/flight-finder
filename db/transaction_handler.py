from db.repositories.locales import LocalesRepository
from db.schema import Schema
from sqlalchemy import insert

def insert_locales(locales):
    schema = Schema()
    schema.drop_all_tables()
    schema.create_all_tables()

    with schema.create_transaction() as tx:
        table = tx.schema.tables['locales']

        for local in locales:
            print('Emuglio')
            print(local)
            local_dto = {
                'code': local['code'],
                'name': local['name']
            }
            query = insert(table).values(local_dto)
            tx.conn.execute(query)
        locales = LocalesRepository(tx).find_all()
        print(locales.fetchall())