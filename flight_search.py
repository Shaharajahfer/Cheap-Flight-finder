from pprint import pprint

from flight_data import FlightData
import requests

TEQUILA_API_KEY = "###############"
TEQUILA_URL = "https://tequila-api.kiwi.com/"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):      #Get IATA code
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(
            url=f"{TEQUILA_URL}locations/query",
            headers=headers,
            params=params
        )

        results = response.json()["locations"]
        #    print(response.json())
        code = results[0]["code"]
        return code


    def search_flight(self, origin_city_code, destination_city_code, from_time, to_time):

        header = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,        #Looking for round trips that return between 7 and 28 days in length.
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,              #Direct flight
            "curr": "GBP",                  #Currency of the price we get back should be in GBP.
            "max_stopovers": 0
        }

        response = requests.get(
            url=f"{TEQUILA_URL}v2/search",
            headers=header,
            params=query
        )

        try:
            data = response.json()["data"][0]
            #pprint(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city = data["cityFrom"],
            origin_airport = data["flyFrom"],
            destination_city = data["cityTo"],
            destination_airport = data["flyTo"],
            out_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
