import requests
from pprint import pprint

API_KEY = "cd5b3262f4a1a6071dcf78eba8229b22"

def check_coordinates(city, API_KEY):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    # print(response.status_code)
    # pprint(response.json()) 
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    city = response.json()[0]['name']
    country = response.json()[0]['country']
    # lon - dł. geograficzna
    # name - nazwa miasta
    # country - państwo
    return lat, lon, city, country

city = input("Wprowadź miasto startowe: ")
city_2 = input("Wprowadź miasto docelowe: ")
print(check_coordinates(city, API_KEY))
print(check_coordinates(city_2, API_KEY))