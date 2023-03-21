# PRACTICE. Privatbank.

import requests


def test_status_code(user_link: str):
    
    if user_link.ok:
        return True
    else: 
        False


def exchange_rate():

    # Privatbank returns only EUR and USD.

    res_privatbank = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

    if test_status_code(res_privatbank):  # Returns True if status_code is less than 400, otherwise False
        currencies = {
            'USD': '🇺🇸',
            'EUR': '🇪🇺'
            }
        rates = []
        for obj in res_privatbank.json():
            if obj['ccy'] in currencies and obj not in rates:
                rates.append(obj)
        for obj in rates:
            print(f"Currency: {currencies[obj['ccy']]}, purchase: {obj['buy']}, sales: {obj['sale']}")
    else:
        print("Operation failed because there is no response from the server.")


print(exchange_rate())

# task 1. Create a program that will ask user to search a word.
# Search this word in Giphy (use their API).
# Return links to these GIFs as a result.

user_search = str(input('Enter your searching query: '))


def search_for_gif(user_input: str):

    url_link = 'https://api.giphy.com/v1/gifs/search?api_key=xN6xme9ip5xIPWwVqJ454Vz9DdCcieFI'

    user_data = {
        'q': user_search,
        'limit': 3,
        'offset': 0,
        'rating': 'g',
        'lang': 'en'
        }

    res_search = requests.get(url_link, params=user_data)

    if test_status_code(res_search):
        gif_response = res_search.json().get('data')

        # print(json.dumps(gif_response, indent = 4))

        print(f"You enter '{user_search}' ")

        gif_list = []

        for gif in range(len(gif_response)):
            for key in gif_response[gif]:
                if key == 'url':
                    gif_list.append(gif_response[gif][key])
        return gif_list
    else:
        print("Resource didn't responde.")


print(*search_for_gif(user_search), sep="\n")

# task 2. Take API-weather, parse and display the weather from the user
# (user enters a location, this location will return the weather, humidity, etc.)

user_city = str(input('Enter your city: '))


def get_weather(user_input: str):

    url_link = 'http://api.openweathermap.org/data/2.5/weather?'

    api_key = '799d8eb6a91da7681c2389c4d944c310'

    full_url = url_link + "appid=" + api_key + "&q=" + user_input

    response = requests.get(full_url)

    parcing = response.json()

    if test_status_code(response):
        rsp_weather = parcing.get("weather")
        rsp_main = parcing.get("main")
        rsp_wind = parcing.get("wind")
        current_temperature = rsp_main["temp"]
        current_pressure = rsp_main["pressure"]
        current_humidity = rsp_main["humidity"]
        current_weather = rsp_weather[0]["description"]
        current_wind = rsp_wind["speed"]
        return ("\n Weather description: " +
                str(current_weather) +
                "\n temperature (in kelvin) = " +
                str(current_temperature) +
                "\n atmospheric pressure (in hPa) = " +
                str(current_pressure) +
                "\n humidity (in percentage) = " +
                str(current_humidity) +
                "\n wind (m/s) = " +
                str(current_wind))
    else:
        print("Couldn't found your city.")


print(get_weather(user_city))

# Take out all astronauts (number and names).


def astros():

    url_link = 'http://api.open-notify.org/astros.json'

    response = requests.get(url_link)

    parcing = response.json()

    if test_status_code(response):
        astr_number = parcing.get("number")
        people = parcing.get("people")
        astr_people = []
        for astr in range(len(people)):
            for key in people[astr]:
                if key == "name":
                    astr_people.append(people[astr][key])
        print(f"Number of astronauts: {astr_number}, their names: ", *astr_people, sep = "\n")
    else:
        print("Astronauts are in orbit and inaccessible.")


print(astros())
