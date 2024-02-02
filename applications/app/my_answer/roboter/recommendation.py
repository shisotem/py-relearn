import csv


def recommend_restaurant(index):
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        row = rows[index]

    print(f"< I recommend {row['Name']} restaurant.")


def is_preferred():
    while True:
        res = input('< Do you like it? [y/n]\n> ')
        if res == 'Yes' or 'yes' or 'y':
            return True
        if res == 'No' or 'no' or 'n':
            return False
        else:
            print('< Invalid input.')


def update_next_recommendation_index(prev_index):
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        max_row_index = sum(1 for row in reader) - 1  # arg: generator expression
        if prev_index == max_row_index:
            return -1
        else:
            return prev_index + 1
