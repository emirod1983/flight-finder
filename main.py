from business.business import get_flights, handle_flights
from db.transaction_handler import initialize_schema
from flask import Flask, render_template

# run app with: flask --app main run --debug
app = Flask(__name__)

@app.route("/get/")
def flights():
    flights = get_flights()
    handle_flights(flights)
    return render_template('main.html', input="Flights fetched successfully!")

@app.route("/init_schema/")
def base():
    initialize_schema()
    return render_template('main.html', input="Initialized schema with Skyscanner's currencies, locales and markets")
