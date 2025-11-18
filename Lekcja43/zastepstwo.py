import requests
#
# url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
# response = (requests.status_codes)
# response = (requests.head(url))
# issResponse = requests.get("http://api.open-notify.org/astros.json")
# print(issResponse.text)

API_KEY = 'e44f697adb8a9bbecae7b483968899bb'

#response = requests.get(url)
#print(response.text)

json = """[{'country': 'MA',
'lat': 34.022405,
'local_names': {'am': 'ራባት',
,'الرباط' :'ar'
'be': 'Рабат',
'bg': 'Рабат',
...
...

,'رباط' :'ur'
'vi': 'Rabat',
'vo': 'Ribat',
'zh': '拉巴特'},
'lon': -6.834543,
'name': 'Rabat'}]"""

#name = response.json()[0]["name"]
#print(name)

def check_coordinates(city, API_KEY):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    print(response.status_code)
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]
    city_res = response.json()[0]["name"]
    country = response.json()[0]["country"]
    return lat, lon, city_res, country

#print(check_coordinates("Warszawa", API_KEY))

print("Witaj, jestem Mieszko, twój inteligentny asystent podróży!")
origin_city = input("Podaj nazwę miasta, z którego pochodzisz: ")
destination_city = input("Podaj nazwę miasta, do którego się udajesz: ")

origin_lat, origin_lon, origin_name, origin_country = check_coordinates(origin_city, API_KEY)
destination_lat, destination_lon, destination_name, destination_country = check_coordinates(destination_city, API_KEY)

print(f"Podróż z: {origin_name}, {origin_country} do {destination_name}, {destination_country}")
print(f"Współrzędne początkowe: {origin_lat}N, {origin_lon}W")
print(f"Współrzędne docelowe: {destination_lat}N, {destination_lon}W")

def get_weather_info(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=PL&units=metric"
    response = requests.get(url)
    response_json = response.json()
    
    # for k in response_json.keys():
    #     print(f"{k}: {response_json[k]}")

    weather = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']
    return weather, temperature, pressure, humidity

weather, temperature, pressure, humidity = get_weather_info(destination_lat, destination_lon)

print(f"Pogoda: {weather}")
print(f"Temperatura: {temperature} C")
print(f"Ciśnienie: {pressure} hPa")
print(f"Wilgotność: {humidity}%")

def get_country_data(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    #print(response.json())
    response_json = response.json()[0]
    # for k in response_json.keys():
    #     print(f"{k}: {response_json[k]}")
    country_name = response_json['name']['common']
    currency = list(response_json['currencies'].keys())[0]
    return country_name, currency

def pretty_print(json):
    for k in json.keys():
        print(f"{k}: {json[k]}")

ori_name, ori_curr = get_country_data(origin_country)
print(f"Państwo startowe: {ori_name}, Waluta p. startowego: {ori_curr}")
dest_name, dest_curr = get_country_data(destination_country)
print(f"Państwo docelowe: {dest_name}, Waluta p. docelowego: {dest_curr}")

def get_currency_ratio(ori_curr, dest_curr):
    if ori_curr != "PLN":
        url = f"https://api.nbp.pl/api/exchangerates/rates/B/{ori_curr}/"
        response = requests.get(url)
        #pretty_print(response.json())
        origin_rate = response.json()['rates'][0]['mid']

    else:
        origin_rate = 1

    if dest_curr != "PLN":
        url = f"https://api.nbp.pl/api/exchangerates/rates/B/{dest_curr}/"
        response = requests.get(url)
        #pretty_print(response.json())
        dest_rate = response.json()['rates'][0]['mid']

    else:
        dest_rate = 1
    
    return dest_rate / origin_rate

ratio = get_currency_ratio(ori_curr, dest_curr)
print(f"Kurs wymiany walut: {ratio}")