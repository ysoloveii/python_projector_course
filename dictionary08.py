# PRACTICE 1. 

# Create emtpy dictionary named en_ua_dictionary.

en_ua_dictionary = {}

# Add few key-value pairs to the dictionary. Example: 'red': 'червоний'

en_ua_dictionary = {
    'red' : 'червоний',
    'green' : 'зелений',
    'yellow' : 'жовтий',
}

# Check if the dictionary contains key 'blue' and 'purple'. If not, set their values to unknown. 

if 'blue' in en_ua_dictionary and 'purple' not in en_ua_dictionary:
    print ("Blue is present.")
    en_ua_dictionary['purple'] = 'Unknown'
elif 'purple' in en_ua_dictionary and 'blue' not in en_ua_dictionary:
    print ("Purple is present.")
    en_ua_dictionary['blue'] = 'Unknown'
else: 
    en_ua_dictionary['blue'] = 'Unknown'
    en_ua_dictionary['purple'] = 'Unknown'

# Create a loop over existing values and print them to the console in the following format: Red in Ukrainian is червоний.

for key, value in en_ua_dictionary.items():
    print (f'{key} in Ukranian is {value}')

# Delete all key-values pairs from the dictionary if the lenght of value is lower than 5. 

delete_key = list()
for key in en_ua_dictionary:
    if len(str(key)) > 5:
        delete_key.append(key)
for i in delete_key:
    del en_ua_dictionary[i]

print (en_ua_dictionary)

# Write a game where user should guess of a capital of the country that you have in your dictionary.
# You should show user a random country from the list and ask him to guess the capital. 
# If user input right capital, print "You are right!", add him a point and ask him to guess another country. 
# If not, you should ask again. User should be able to quit the game by typing "exit". You should print current score after each round. 
# Also, you should print the final score before user quit the game.

import random as rd

capitals = { 
    'Ukraine': 'Kyiv', 
    'France': 'Paris', 
    'Germany': 'Berlin', 
    'Italy': 'Rome', 
    'USA': 'Washington', 
    'Canada': 'Ottawa', 
    'Switzerland': 'Bern', 
    'Austria': 'Vienna', 
    'Belgium': 'Brussels', 
    'Sweden': 'Stockholm', 
    'Norway': 'Oslo', 
    'Denmark': 'Copenhagen', 
    'Finland': 'Helsinki', 
    'Poland': 'Warsaw', 
    'Romania': 'Bucharest', 
    'Bulgaria': 'Sofia', 
    'Greece': 'Athens'
    }

score = 0
while True:
    player_choice = input ('Play (p) or exit (e)?: ').strip().lower()
    match player_choice:
        case 'p':
            country = rd.choice(list(capitals.keys()))
            capital = (capitals[country])
            user_choice = input (f'Try to guess capital of {country}: ').strip().lower()
            user_choice = user_choice.capitalize()
            if isinstance(user_choice, str):
                if user_choice == capital:
                    print ("You're right!")
                    score += 1
                    print (f'Your score: {score}')
                else:
                    print ("Oh no, it's wrong :( ")
            else: 
                print ('Your input was not a string.')
        case 'e':
            print (f"Your score was {score}. Thank you for game!")
            break
        case _:
            print ("I didn't understand your choice. Use option p or e.")



