import sys
import csv

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.residual_edge = None

    def __repr__(self):
        return f"<Edge start:{self.start} end:{self.end} capacity:{self.capacity}>"

    def __str__(self):
        return f"{self.start},{self.end}"



class flow_networks:

    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_edge(self, start, end, capacity):
        edge = Edge(start,end,capacity)
        residual_edge = Edge(start,end,0)

        edge.residual_edge = residual_edge
        residual_edge.residual_edge = edge

        self.adj[start].append(edge)
        self.adj[end].append(residual_edge)

        self.flow[edge] = 0
        self.flow[residual_edge] = 0


    ''' Reads input file and stores as adjacency matrix with accompanying dictionary for node index '''
    def parse_file(self,file):
        with open(file, mode= 'r') as file:
            csvFile = csv.reader(file)

            # Populate adjacency list
            for line in csvFile:
                if line[0] not in self.adj:
                    self.adj[line[0]] = []
                if line[1] not in self.adj:
                    self.adj[line[1]] = []
                self.add_edge(line[0],line[1],int(line[2]))

    def find_path(self, source, sink, path):
        queue = [(source, path)]
        while queue:
            (source, path) = queue.pop(0)
            for edge in self.adj[source]:
                residual = edge.capacity - self.flow[edge]
                if residual > 0 and edge not in path and edge.residual_edge not in path:
                    if edge.end == sink:
                        return path + [edge]
                    else:
                        queue.append((edge.end, path + [edge]))


    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            # print('path', path)
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.residual_edge] -= flow
            path = self.find_path(source, sink, [])
            # print 'flow', self.flow
        return sum(self.flow[edge] for edge in self.adj[source])


for file in sys.argv[1:]:
    # printing out input file
    print(f'Input File: {file}\n')
    print("Input:")
    with open(file, 'r') as f:
        print(f.read())

    # reading input file
    n = flow_networks()
    n.parse_file(file)

    # run Ford-Fulkerson algorithm on network
    max_flow = (n.max_flow('s','t'))

    # printing out network flow
    print("\nNetwork Flow:")
    for i in n.flow.items():
        if i[0].capacity != 0:
            print(f"{i[0]}\t flow:  {i[1]}/{i[0].capacity}")
    print("\nMax flow in this network is",max_flow)