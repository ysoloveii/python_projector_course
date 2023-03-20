# PRACTICE. Monobank.

import requests

res_monobank = requests.get('https://api.monobank.ua/bank/currency')
res_monobank.status_code

print(res_monobank.status_code, type(res_monobank.status_code))

res_monobank.json()[:5:]

for obj in res_monobank.json():
    print(f'Object is{obj}, \nType is{type(obj)}', end = '\n\n')

my_currencies = {
    980: '🇺🇦',
    840: '🇺🇸',
    978: "🇪🇺",
    826: '🇬🇧',
}

my_rates = []
for obj in res_monobank.json():
    if obj['currencyCodeA'] in my_currencies and obj not in my_rates:
        my_rates.append(obj)

print(my_rates)

for obj in my_rates:
    print(f"Країна: {my_currencies[obj['currencyCodeA']]} Купівля {obj['rateBuy']} Продаж: {obj['rateSell']}")

# Privatbank.


def exchange_rate():

    # Privatbank returns only EUR and USD.

    res_privatbank = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

    if res_privatbank.ok:  # Returns True if status_code is less than 400, otherwise False
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
    gif_response = res_search.json().get('data')

    # print(json.dumps(gif_response, indent = 4))

    print(f"You enter '{user_search}' ")

    gif_list = []

    for gif in range(len(gif_response)):
        for key in gif_response[gif]:
            if key == 'url':
                gif_list.append(gif_response[gif][key])
    return gif_list


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

    if response.ok:
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

    if response.ok:
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
