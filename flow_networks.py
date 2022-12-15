import sys
import csv

network = []

with open(sys.argv[1], mode= 'r') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        network.append([line[0],line[1],int(line[2]),0])


print(f'Input File: {sys.argv[1]}\n')
print("Input:")
for edge in network:
    print(f'{edge[0]},{edge[1]},{edge[2]}')