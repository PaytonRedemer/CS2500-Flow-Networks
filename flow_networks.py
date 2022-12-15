import sys
import csv


max_flow = 0

class flow_networks:

    def __init__(self, file):
        self.file = file
        self.network = []
        self.residual_network = []
        self.nodes_index = {}
        self.parse_file()

    ''' Reads input file and stores as adjacency matrix with accompanying dictionary for node index '''
    def parse_file(self):
        with open(self.file, mode= 'r') as file:
            csvFile = csv.reader(file)

            # Create dictionary to assign vertices with an index
            for line in csvFile:
                print(f'{line[0]},{line[1]},{line[2]}')
                if line[0] not in self.nodes_index:
                    self.nodes_index[line[0]] = len(self.nodes_index)
                if line[1] not in self.nodes_index:
                    self.nodes_index[line[1]] = len(self.nodes_index)

            # Create an empty adjacency matrix and residual netowrk matrix based on number of nodes
            self.network = [[0 for x in range(len(self.nodes_index))] for y in range(len(self.nodes_index))]
            self.residual_network = [[0 for x in range(len(self.nodes_index))] for y in range(len(self.nodes_index))]

            file.seek(0) # Jump to beginning of file again

            # Populate adjacency matrix
            for line in csvFile:
                self.network[self.nodes_index[line[0]]][self.nodes_index[line[1]]] = int(line[2])



# printing out input file
print(f'Input File: {sys.argv[1]}\n')
print("Input:")

n = flow_networks(sys.argv[1])

print(n.ford_fulkerson())

# print(len(n.network))

# TODO: Edmonds-Karp here

# printing out network flow
# print("\nNetwork Flow:\n")
# for edge in network:
#     print(f'{edge[0]},{edge[1]}\tflow: {edge[3]}/{edge[2]}')
# print("\nMax flow in this network is",max_flow)