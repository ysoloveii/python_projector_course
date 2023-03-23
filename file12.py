# task 1. a) Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# b) To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains name of the file and number in that file.

import random as rd
import csv

for i in range(0, 26):
    alphabet_letter = chr(65+i)
    with open(f"{alphabet_letter}.txt", 'w') as file, open("summary.txt", "a") as file_sum:
        rnd_number = rd.randint(1, 100)
        file.write(str(rnd_number))
        file_sum.write(f"{file.name} : {rnd_number}\n")
        print(f"{alphabet_letter}.txt")

# task 2. Create file with some content.
# Create second file and copy content of the first file to the second file in upper case.

with open("some_content.txt", "w") as file:
    file.write("Мої предки були не вбогі \n На пісні та свячені ножі — \nЗ моїх предків, хвалити Бога, \nЗаволокам ніхто не служив!")

with open("some_content.txt", "r") as firstfile, open("copy_content.txt", "a") as secondfile:
    for line in firstfile:
        secondfile.write(line)

# task 3. Write a program that will simulate user score in a game.
# Create a list with 5 player's names. After that simulate 100 games for each player.
# As a result of the game create a list with player's name and his score (0-1000 range).
# And save it to a CSV file. File should looks like this

user_names = ["Luke", "Han", "Leia", "Obi-Wan", "R2-D2"]


def game_simulate(users):

    with open("user_score.csv", "a") as file:
        header = ['Player name', 'Score']
        writer = csv.writer(file, delimiter=",")
        writer.writerow(header)
        user_score = []
        for i in range(0, 100):
            for player in users:
                score = str(rd.randint(0, 1000))
                user_score.append([f"{player}", f"{score}"])
            writer.writerows(user_score)
        print(user_score)


game_simulate(user_names)

# task 4. Write a script that reads the data from previous CSV file and creates
# a new file called high_scores.csv where each row contains the player name and
# their highest score. Final score should sorted by descending of highest score.


def find_max(user_rows, name):

    score = []
    for index in user_rows:
        if index[0] == name:
            score.append(index[1])
    return (max(score))


with open("user_score.csv", "r") as firstfile, open("high_score.csv", "a") as secondfile:
    reader = csv.reader(firstfile)
    rows = []
    for row in reader:
        rows.append(row)

    names_dict = {}
    for name in user_names:
        names_dict[name] = find_max(rows, str(name))

    sort_dict = {}

    sorted_keys = sorted(names_dict, key=names_dict.get, reverse=True)

    for w in sorted_keys:
        sort_dict[w] = names_dict[w]

    high_header = ['Player name', 'Highest score']
    writer = csv.writer(secondfile, delimiter=",")
    writer.writerow(high_header)
    for key in sort_dict.keys():
        secondfile.write("%s, %s\n" % (key, sort_dict[key]))
        