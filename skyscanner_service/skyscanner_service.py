from config import api_host, get_headers, post_headers
from crosscutting.constants import HTTP_GET, HTTP_POST
from skyscanner_service.payload_builder import get_payload
import http.client

def get_flights_synced(date_from):
    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_POST, "/v3e/flights/live/search/synced", get_payload(date_from), post_headers)
    return conn.getresponse()

def get_dataset(dataset_name):
    url = "/v3/culture/"+dataset_name
    if dataset_name == 'markets':
        url += "/es-ES"

    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_GET, url, headers=get_headers)
    return conn.getresponse()
