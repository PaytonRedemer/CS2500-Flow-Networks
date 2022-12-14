import sys
import csv

network = []

print(sys.argv[1])

with open(sys.argv[1], mode= 'r') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        network.append([line[0],line[1],int(line[2]),0])

print(network)
