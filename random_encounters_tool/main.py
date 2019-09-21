from pathlib import Path
from random import randrange
import json
import click

def main():
    path = Path("./")
    file_to_open = path / "encounter_data.json"

    with open(file_to_open) as json_file:
        encounters = json.load(json_file)

    # print(encounters)
    # pick a random encounter
    random_encounter_number = randrange(0, len(encounters['encounter_list']))
    print(random_encounter_number)
    print(encounters['encounter_list'][random_encounter_number])




if __name__ == '__main__':
    main()
