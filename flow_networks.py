import sys
import csv

class flow_networks:

    def __init__(self, file):
        self.file = file
        self.network = []
        self.nodes_index = {}
        self.parse_file()
        self.vertices = len(self.network)

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

    def BFS(self, s, t, parent):
        visited = [False]*(self.vertices)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.network[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.vertices)

        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.network[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.network[u][v] -= path_flow
                self.network[v][u] += path_flow
                v = parent[v]

        return max_flow

# printing out input file
print(f'Input File: {sys.argv[1]}\n')
print("Input:")

n = flow_networks(sys.argv[1])

source = n.nodes_index['s']
sink = n.nodes_index['t']

max_flow = n.FordFulkerson(source,sink)


# printing out network flow
# print("\nNetwork Flow:\n")
# for edge in n.network:
#     print(f'{edge[0]},{edge[1]}\tflow: {edge[3]}/{edge[2]}')
print("\nMax flow in this network is",max_flow)