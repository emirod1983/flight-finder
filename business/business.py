import datetime
from crosscutting.constants import filename
from crosscutting.helpers import get_json_dict, dump_to_file
from skyscanner_service.skyscanner_service import get_flights_synced, get_locales, get_markets, get_currencies

def get_flights():
    date_from = datetime.date(2023, 7, 15)
    source_data = get_flights_synced(date_from)
    json_dictionary = get_json_dict(source_data)
    dump_to_file(filename, json_dictionary)
