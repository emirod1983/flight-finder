import json

def get_payload():
    date = {}
    date['year'] = 2023
    date['month'] = 7
    date['day'] = 15

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
