import sys
import networkx as nx
import time

def main(name:str, gridsize:int, task1_limit:int):
    path = "inputs/day18/"
    
    with open(path+name+".txt") as file:
        data = [tuple(int(i) for i in line.strip().split(",")[::-1]) for line in file]
    
    #Task 1
    start = time.time()
    
    #Back to Dijkstra again - in this case might be worth it to just implement it myself
    grid = nx.Graph()
    grid.add_edges_from({((i, j), (i+1, j)) for i in range(gridsize-1) for j in range(gridsize)})
    grid.add_edges_from({((i, j), (i, j+1)) for i in range(gridsize) for j in range(gridsize-1)})
    grid.remove_nodes_from(data[:task1_limit])
    
    shortest_path = nx.dijkstra_path(grid, (0, 0), (gridsize-1, gridsize-1))
    
    end = time.time()
    
    print("Shortest path length after {} bytes have fallen:".format(task1_limit), len(shortest_path)-1)
    print("Runtime:", end-start)
    
    #Show grid to check
    for y in range(gridsize):
        print("".join([('#' if (x, y) in data[:task1_limit] else 'O' if (x, y) in shortest_path else '.') for x in range(gridsize)]))
    
    return

if __name__ == "__main__":
    #Run test input
    main("test", gridsize=7, task1_limit=12)
    #Run target input
    main("input", gridsize=71, task1_limit=1024)
    sys.exit()