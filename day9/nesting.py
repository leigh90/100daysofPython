capitals = {
    'France': "Paris",
    "Germany": "Berlin",
}
# nesting lists in a dictionary
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"],

}
# nesting dictionary in  a dictionary

travel_log = {
    "France": {
        "cities_visited":["Paris","Lille","Dijon"], 
        'total_visits': 8
        },
    "Germany": {
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits": 5,
        }

}

# nesting dictionaries inside lists
travel_log = [
    {
        "country": "France",
        "cities_visited":["Paris","Lille","Dijon"], 
        'total_visits': 8,
        }
    {
        "country": "Germany", 
        "cities_visited":["Berlin","Hamburg","Stuttgart"]},
        "total_visits": 5,
        }

]

