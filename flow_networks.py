import sys
import csv

network = []
nodes_index = {}
max_flow = 0



# printing out input file
print(f'Input File: {sys.argv[1]}\n')
print("Input:")

# reading in input file
with open(sys.argv[1], mode= 'r') as file:
    csvFile = csv.reader(file)

    # Create dictionary to assign vertices with an index
    for line in csvFile:
        print(f'{line[0]},{line[1]},{line[2]}')
        if line[0] not in nodes_index:
            nodes_index[line[0]] = len(nodes_index)
        if line[1] not in nodes_index:
            nodes_index[line[1]] = len(nodes_index)

    # Create an empty adjacency matrix based on number of nodes
    network = [[0 for x in range(len(nodes_index))] for y in range(len(nodes_index))]

    file.seek(0) # Jump to beginning of file again

    # Populate adjacency matrix
    for line in csvFile:
        network[nodes_index[line[0]]][nodes_index[line[1]]] = int(line[2])


# TODO: Edmonds-Karp here

# printing out network flow
# print("\nNetwork Flow:\n")
# for edge in network:
#     print(f'{edge[0]},{edge[1]}\tflow: {edge[3]}/{edge[2]}')
# print("\nMax flow in this network is",max_flow)