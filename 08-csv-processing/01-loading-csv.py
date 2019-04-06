import csv
# https://docs.python.org/3/library/csv.html
filename = 'example data - bicycle infrastructure funding in Kraków.csv'
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['year'], row['money actually spend [millions PLN]'])
