import datetime
from db.transaction_handler import insert_locales
from crosscutting.constants import filename
from crosscutting.helpers import get_json_dict, dump_to_file
from flask import Flask, render_template
from skyscanner_service.skyscanner_service import get_flights_synced, get_locales, get_markets, get_currencies

# run app with: flask --app main run --debug
app = Flask(__name__)

@app.route("/get/")
def get_flights():
    date_from = datetime.date(2023, 7, 15)
    source_data = get_flights_synced(date_from)
    json_dictionary = get_json_dict(source_data)
    dump_to_file(filename, json_dictionary)

    return render_template('main.html', input="Flights fetched successfully!")

@app.route("/locales/")
def locales():
    response = get_locales()
    json_dictionary = get_json_dict(response)
    insert_locales(json_dictionary['locales'])
    # dump_to_file('dumps/locales.json', json_dictionary)

    return render_template('main.html', input="Fetched locales")

@app.route("/markets/")
def markets():
    response = get_markets()
    json_dictionary = get_json_dict(response)
    dump_to_file('dumps/markets.json', json_dictionary)

    return render_template('main.html', input="Fetched markets")

@app.route("/currencies/")
def currencies():
    response = get_currencies()
    json_dictionary = get_json_dict(response)
    dump_to_file('dumps/currencies.json', json_dictionary)

    return render_template('main.html', input="Fetched currencies")
