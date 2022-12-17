#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Payton Redemer
File: flow_networks.py
Purpose: Find max flow of flow network input file
Note: Basic Inspiration on storing graph was from https://brilliant.org/wiki/ford-fulkerson-algorithm/
"""

import sys
import csv
import glob

DEBUG = False

class Edge:
    # Constructor
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.residual_edge = None

    # Print edge
    def __repr__(self):
        return f"<Edge start:{self.start} end:{self.end} capacity:{self.capacity}>"

    # Print readable edge
    def __str__(self):
        return f"{self.start},{self.end}"


class flow_networks:
    # Constructor
    def __init__(self):
        self.adjacency = {}
        self.flow = {}

    def add_edge(self, start, end, capacity):
        """
        Add edge to flow network

        Precondition: start != end and capacity > 0

        Parameters
        ----------
        start : str
            Start vertex of edge
        end : str
            End vertex of edge
        capacity : int
            Max capacity of edge

        Postcondition: Edge is added to adjacency list and flow list
        """
        if start == end:
            raise ValueError("Edges that are loops cannot be added")

        edge = Edge(start,end,capacity)
        residual_edge = Edge(start,end,0)

        edge.residual_edge = residual_edge
        residual_edge.residual_edge = edge

        self.adjacency[start].append(edge)
        self.adjacency[end].append(residual_edge)

        self.flow[edge] = 0
        self.flow[residual_edge] = 0


    def parse_file(self,file):
        """
        Reads input file and stores as adjacency list and a list with flow for each edge

        Precondition: file be a valid file path and the file must be in the format as specified in the README

        Parameters
        ----------
        file : str
            File path to input file

        Postcondition: flow_networks is populated based on the input file
        """
        with open(file, mode= 'r') as file:
            csvFile = csv.reader(file)

            # Populate adjacency list
            for line in csvFile:
                # Add unknown vertex to self.adjacency
                if line[0] not in self.adjacency:
                    self.adjacency[line[0]] = []
                if line[1] not in self.adjacency:
                    self.adjacency[line[1]] = []

                self.add_edge(line[0],line[1],int(line[2]))

    def find_path(self, start, end, path):
        """
        Find augmenting path in flow network using breadth first search

        Precondition: start != end

        Parameters
        ----------
        start : str
            Start vertex of edge
        end : str
            End vertex of edge
        path : list[Edge]
            List vertices of a path in order

        Postcondition: If a path exists, path is filled with a valid path
        """
        queue = [(start, path)]
        while queue:
            (start, path) = queue.pop(0)
            for edge in self.adjacency[start]:
                residual = edge.capacity - self.flow[edge]
                if residual > 0 and edge not in path and edge.residual_edge not in path:
                    if edge.end == end:
                        return path + [edge]
                    else:
                        queue.append((edge.end, path + [edge]))

    def cut_flow(self):
        """
        Loop invariant for Ford-Fulkerson

        Parameters
        ----------
        source : str
            Source vertex of network
        sink : str
            Sink vertex of network

        Returns truth value if all cuts that make s and t disjoint have the same net flow
        """
        net_flow = 0
        for i in self.flow:
            net_flow += self.flow[i]
        return net_flow == 0

    def ford_fulkerson(self, source, sink):
        """
        Run Ford-Fulkerson on flow network

        Precondition: adjacency and flow lists are configured using parse_file() and there must be a distinct source and sink

        Parameters
        ----------
        source : str
            Source vertex of network
        sink : str
            Sink vertex of network

        Postcondition: Returns max flow of network and modifies flow list to reflect max flow
        """
        if DEBUG:
            assert self.cut_flow()
        path = self.find_path(source, sink, [])
        while path != None:
            if DEBUG:
                assert self.cut_flow()
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.residual_edge] -= flow
            path = self.find_path(source, sink, [])
        if DEBUG:
            assert self.cut_flow()
        return sum(self.flow[edge] for edge in self.adjacency[source])

# If no command arguments are specified
if len(sys.argv) == 1:
    files = glob.glob('network*.txt')
# Add all command arguments to file
else:
    files = sys.argv[1:]

# Run Ford-Fulkerson on each file
for file in files:
    # reading input file
    n = flow_networks()
    n.parse_file(file)

    # run Ford-Fulkerson algorithm on network
    max_flow = (n.ford_fulkerson('s','t'))

    # Output to file
    with open("output_"+file[:-4]+".txt", 'w') as f:
        # printing out input file
        print(f'Input File: {file}\n', file=f)
        print("Input:", file=f)
        with open(file, 'r') as input:
            print(input.read(), file=f)

        # printing out network flow
        print("\nNetwork Flow:", file=f)
        for i in n.flow.items():
            if i[0].capacity != 0:
                print(f"{i[0]}\t flow:  {i[1]}/{i[0].capacity}", file=f)
        print(f"\nMax flow in this network is {max_flow}", file=f)