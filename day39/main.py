# Initialize objects
from datetime import datetime
from email.utils import decode_params
from flight_search import FlightSearch
from notification import SMSNotification
from wishlist_data import Wishlist

home = 'NBO'
data = Wishlist()
flight_search = FlightSearch()
alert = SMSNotification()

# TODO Get wishlist data
locales = data.get_wishlist_data()
print(locales)
for potential in locales:
    dest = potential['city']
    iata = potential['iataCode']
    best = potential['lowestPrice']
    # depature_date =

    all_flight_data = flight_search.get_flights(home=home, destination=iata, best_price=best)
    # print(all_flight_data[0][''])
    flight_destination = all_flight_data[0]['flyTo']
    flight_depature = all_flight_data[0]['cityTo']
    flight_price = all_flight_data[0]['price']
    dt_string = all_flight_data[0]['local_departure']
    # departure_date = datetime.strptime(dt_string,"%d/%m/%Y %H:%M:%S" )
    # departure_date = datetime.fromisoformat(dt_string)
    departure_date = dt_string[0:10]
    departure_time = dt_string[11:16]
    # print(f"Fly to {flight_destination} from {flight_depature} for {flight_price} Euros on {departure_date} at {departure_time}")


    if flight_price <= best:
        flight_notification = f"Fly to {dest}-{flight_destination} - from {home} for {flight_price} Euros on {departure_date} at {departure_time}"
        alert.send_message(flight_notification=flight_notification)
