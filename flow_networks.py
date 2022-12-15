import sys
import csv

class edge:
    def __init__(self, start, end, capacity, flow = 0):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = flow

    def __repr__(self):
        return f"<edge start:{self.start} end:{self.end} capacity:{self.capacity} flow:{self.flow}>"

    def __str__(self):
        return f"{self.start},{self.end}\tflow:\t{self.flow}/{self.capacity}"



class flow_networks:

    def __init__(self, file):
        self.file = file
        self.network = []
        self.parse_file()

    ''' Reads input file and stores as adjacency matrix with accompanying dictionary for node index '''
    def parse_file(self):
        with open(self.file, mode= 'r') as file:
            csvFile = csv.reader(file)

            # Populate adjacency list
            for line in csvFile:
                self.network.append(edge(line[0],line[1], int(line[2])))



# printing out input file
print(f'Input File: {sys.argv[1]}\n')
print("Input:")

n = flow_networks(sys.argv[1])
max_flow = 0

# print(n.ford_fulkerson())

# TODO: Ford-Fulkerson here

# printing out network flow
print("\nNetwork Flow:")
for edge in n.network:
    print(edge)
print("\nMax flow in this network is",max_flow)