import sys
import numpy as np
import networkx as nx

def main():
    path = "inputs/day16/"
    name = "test"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    maze = set(zip(*np.where(data != "#")))
    
    #(Task 1) Make horizontal and vertical edges - I can then connect these via rotations.
    horizontal = {((i, j), (i+1, j)) for (i, j) in maze if (i+1, j) in maze}
    vertical = {((i, j), (i, j+1)) for (i, j) in maze if (i, j+1) in maze}
    
    print(horizontal)
    
    
    return
    
if __name__ == "__main__":
    sys.exit(main())