import csv

with open('dictionary.csv', 'r') as csvfile:
    uncleaned_proxys = list(csv.reader(csvfile))
    print (uncleaned_proxys)