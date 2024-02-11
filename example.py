import sys

from prima_algorithm import PrimsMST

prims = PrimsMST()

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst = prims.find_min_spanning_tree(graph)

print("The edges of the minimum spanning tree:")
for edge in mst:
    print(edge)