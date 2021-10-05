import requests
from decouple import config

KIWI_API_KEY = config("KIWI_API_KEY")
class FlightSearch():
    def __init__(self):
        self.flight_data = {}
        self.endpoint = "https://tequila-api.kiwi.com/v2/search?"
        self.headers = {
            "apikey" : KIWI_API_KEY,
        }
        self.params = {
            "date_from": "01/10/2021",
            "date_to": "01/04/2022",
            "limit" : 2,
        }
        self.all_flights = []


    def get_flights(self, home, destination, best_price ):
        """
        Call the flight api to get flights for specific destinations at the best price
        """
        self.params.update({"fly_from": home, "fly_to":destination, "price_to": best_price} )
        response = requests.get(url=self.endpoint,params=self.params, headers=self.headers)
        flight_data = response.json()
        # print(flight_data['data'])
        # import pdb; pdb.set_trace()
        self.all_flights = flight_data['data']
        # print(self.all_flights) 
        return self.all_flights




# search = FlightSearch()
# search.get_flights('NBO', 'UKA', 46)