import csv

from roboter import utils


def get_restaurant_vote_count(new_restaurant):
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if new_restaurant == row['Name']:
                return int(row['Count'])
        return 0


def add_restaurant_vote(new_restaurant):
    with open('ranking.csv', 'a') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames)

        if not utils.is_data_present('ranking.csv'):
            writer.writeheader()

        current_vote_count = get_restaurant_vote_count(new_restaurant)
        if current_vote_count == 0:
            writer.writerow({'Name': new_restaurant, 'Count': 1})
        else:
            writer.writerow({'Name': new_restaurant, 'Count': current_vote_count + 1})


def sort_restaurant():
    with open('ranking.csv', 'r+') as csv_file:
        reader = csv.DictReader(csv_file)
        header = next(reader)
        unsorted_list = [row for row in reader]

        sorted_list = sorted(unsorted_list, key=lambda row: row['Count'], reverse=True)

        csv_file.seek(0)
        writer = csv.DictWriter(csv_file, header)
        for row in sorted_list:
            writer.writerow(row)
