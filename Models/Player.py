import csv

with open ("Data/players.csv", 'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        print(row)
        
