import datetime
from crosscutting.constants import filename
from crosscutting.helpers import get_json_dict, dump_to_file, open_from_file
from db.transaction_handler import insert_itineraries
from skyscanner_service.skyscanner_service import get_flights_synced

def get_flights():
    date_from = datetime.date(2023, 7, 15)
    source_data = get_flights_synced(date_from)
    json_dictionary = get_json_dict(source_data)
    dump_to_file(filename, json_dictionary)
    return json_dictionary

def handle_flights(flights):
    # flights = open_from_file('dumps/api_response_2023-04-17-00-35-17.json')
    itineraries = flights['content']['results']['itineraries']
    cheapests = flights['content']['sortingOptions']['cheapest'][:3]

    cheapest_flights_details = { }

    for value in cheapests:
        cheapest_flights_details[value['itineraryId']] = itineraries[value['itineraryId']]

    insert_itineraries(cheapest_flights_details)