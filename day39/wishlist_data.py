import requests


class Wishlist():
    def __init__(self):
        self.endpoint = "https://api.sheety.co/50b9f572d8bb9e2b9755ec54abd6fc25/destinations/locations"
        self.wishlist_data = []


    def get_wishlist_data(self): 
        """
        Call the google sheets api to get the list of wishlist destinations and prices
        """
        response = requests.get(url=self.endpoint)
        wishlist_cities = response.json()
        self.wishlist_data = wishlist_cities['locations']
        # import pdb; pdb.set_trace()
        return self.wishlist_data


# data = Wishlist()
# data.get_wishlist_data()
