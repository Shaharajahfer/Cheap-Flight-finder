from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "YOUR_SHEETY_URL"           ## Sheety URL

class DataManager:
    def __init__(self):
        self.destination_data = {}

    # Provide details in google_sheet.. For google sheet management https://sheety.co/
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        #pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    # Update row in google sheet
    def update_destination_codes(self):
        for element in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": element["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{element['id']}", json=new_data)
            #print(response.text)



