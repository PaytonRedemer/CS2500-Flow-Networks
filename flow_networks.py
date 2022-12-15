import sys
import csv

network = []
max_flow = 0

# reading in input file
with open(sys.argv[1], mode= 'r') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        network.append([line[0],line[1],int(line[2]),0])

# printing out input file
print(f'Input File: {sys.argv[1]}\n')
print("Input:")
for edge in network:
    print(f'{edge[0]},{edge[1]},{edge[2]}')

# TODO: Ford-Fulkerson here

# printing out network flow
print("\nNetwork Flow:\n")
for edge in network:
    print(f'{edge[0]},{edge[1]}\tflow: {edge[3]}/{edge[2]}')
print("\nMax flow in this network is",max_flow)