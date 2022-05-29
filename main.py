
from datetime import datetime, timedelta
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORG_CITY = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()   # Get google sheet details
print(sheet_data)

# Getting IATA code for cities in google sheet
for element in sheet_data:
    if element["iataCode"] == "":
        flight_search = FlightSearch()
        element["iataCode"] = flight_search.get_destination_code(element["city"])
        print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data   #Updating google sheet
data_manager.update_destination_codes()

#Searching for flights
now = datetime.now()
tomorrow = now + timedelta(days=1)
tomorrow = tomorrow.strftime("%d/%m/%Y")

date_after_6months = now + timedelta(days=6 * 30)
date_to = date_after_6months.strftime("%d/%m/%Y")

flight_search = FlightSearch()
for element in sheet_data:
    flight = flight_search.search_flight(ORG_CITY, element["iataCode"], tomorrow, date_to)
    if flight is not None:
        if element["lowestPrice"] >= flight.price:
            print(f"Low price is available for {element['city']}")
            notification_manager = NotificationManager()
            notification_manager.send_sms(msg=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
        else:
            print(f"No flights with lowest price to {element['city']}")










