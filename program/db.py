import os
import csv

FILENAME = "user_data.csv"

def save(values):
    
    if os.path.exists(FILENAME):
        mode = 'a' # append if already exists
    else:
        mode = 'w' # make a new file if not
        columns = list(values.keys())
        with open(FILENAME, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
         

    with open(FILENAME, mode) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writerow(values)

def retrieve():
    if os.path.exists(FILENAME):
        with open(FILENAME) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            values = list(csv_reader)
        return values
    else:
        return []
