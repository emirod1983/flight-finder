from config import api_host, get_headers, post_headers
from crosscutting.constants import HTTP_GET, HTTP_POST
from skyscanner_service.payload_builder import get_payload
import http.client

def get_flights_synced():
    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_POST, "/v3e/flights/live/search/synced", get_payload(), post_headers)
    return conn.getresponse()

def get_locales():
    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_GET, "/v3/culture/locales", headers=get_headers)
    return conn.getresponse()

def get_markets():
    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_GET, "/v3/culture/markets/es-ES", headers=get_headers)
    return conn.getresponse()

def get_currencies():
    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_GET, "/v3/culture/currencies", headers=get_headers)
    return conn.getresponse()
