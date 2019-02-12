import csv
data = [["abacki", 181],
			["babacki", 8],
			["cabacki", 1],
			["dabacki", 81],
			["ebacki", 111],
			]
# https://docs.python.org/3/library/csv.html
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)