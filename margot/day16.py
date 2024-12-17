import sys
import numpy as np
import networkx as nx

def main():
    path = "inputs/day16/"
    name = "test"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    maze = set(zip(*np.where(data != "#")))
    
    #Something w/ pathfinding/Dijkstra's, but not in the mood for this right now.
    
    
    return
    
if __name__ == "__main__":
    sys.exit(main())