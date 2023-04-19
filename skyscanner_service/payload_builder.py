import datetime
import json

# Airport codes: https://www.andiamo.co.uk/resources/iso-language-codes/
def get_payload(date_from):
    date = {}
    date['year'] = date_from.year
    date['month'] = date_from.month
    date['day'] = date_from.day

    originPlaceId = {}
    originPlaceId['iata'] = 'EZE'

    destinationPlaceId = {}
    destinationPlaceId['iata'] = 'FCO'

    leg = {}
    leg['originPlaceId'] = originPlaceId
    leg['destinationPlaceId'] = destinationPlaceId
    leg['date'] = date
    queryLegs = []
    queryLegs.append(leg)


    query = {}
    query['market'] = 'AR'
    query['locale'] = 'es-ES'
    query['currency'] = 'ARS'
    query['queryLegs'] = queryLegs
    query['cabinClass'] = 'CABIN_CLASS_ECONOMY'
    query['adults'] = 1

    payload_raw = {}
    payload_raw['query'] = query

    return json.dumps(payload_raw)
