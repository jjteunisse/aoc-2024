import sys
import numpy as np
import networkx as nx
import time

def main():
    path = "inputs/day16/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    maze = set(zip(*np.where(data != "#")))

    start = time.time()
    #(Task 1) Make undirected graph to find the shortest path. This is intuitive to do in NetworkX.
    graph = nx.Graph()

    #Add vertical connections
    graph.add_edges_from({((i, j, 'V'), (i+1, j, 'V')) for (i, j) in maze if (i+1, j) in maze}, weight=1)

    #Add horizontal connections
    graph.add_edges_from({((i, j, 'H'), (i, j+1, 'H')) for (i, j) in maze if (i, j+1) in maze}, weight=1)

    #Add rotations
    nodes = graph.nodes
    graph.add_edges_from({((i, j, 'H'), (i, j, 'V')) for (i, j) in maze if ((i, j, 'H') in nodes) and ((i, j, 'V') in nodes)}, weight=1000)

    #Define source and target, and add target to graph - we don't care about the direction there. For the source, we need to start facing east.
    source = set(zip(*np.where(data == 'S'))).pop()
    target = set(zip(*np.where(data == 'E'))).pop()
    graph.add_edges_from({(target+('H',), target), (target+('V',), target)}, weight=0)

    #Now it's just a matter of applying Dijkstra's. Since I'm already using NetworkX, no reason not to use its implementation.
    shortest_path = nx.dijkstra_path(graph, source + ('H',), target)
    score = sum([graph.edges[edge]['weight'] for edge in zip(shortest_path[:-1], shortest_path[1:])])

    end = time.time()

    print("Lowest possible score:", score)
    print("Runtime:", end-start)

    #(Task 2) Feels almost like cheating at this point, but that's standard algorithms for you.
    seating_spots = {node[:2] for path in nx.all_shortest_paths(graph, source+('H',), target, weight='weight') for node in path}
    print("Number of good seating spots:", len(seating_spots)) 
    
    return
    
if __name__ == "__main__":
    sys.exit(main())