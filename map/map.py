import requests
from decouple import config

def retrieve_info(city_origin: str, city_destination: str) -> tuple:

    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": config('GOOGLE_API_KEY'),
        "X-Goog-FieldMask": "routes.localized_values,routes.polyline,routes.legs.polyline,routes.travelAdvisory,routes.legs.travelAdvisory", 
    }

    data = {
        "origin": {
            "address": city_origin
        },
        "destination": {
            "address": city_destination
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
        "extraComputations": ["TRAFFIC_ON_POLYLINE"],
        "languageCode": "pt-BR",
        "units": "Metric"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        routes = response_json["routes"][0]
        legs = routes["legs"]
        encoded_polyline = legs[0]["polyline"]["encodedPolyline"]
        jam_info = legs[0]["travelAdvisory"]["speedReadingIntervals"]
        distance = extract_float(routes['localizedValues']['distance']['text'])
    else:
        print(f"Erro: {response.status_code}, {response.text}")

    return encoded_polyline, jam_info, distance

def extract_float(distance_str: str) -> float:
    number_str = ''.join(c for c in distance_str if c.isdigit() or c == ',')
    number_str = number_str.replace(',', '.')
    return round(float(number_str), 2)