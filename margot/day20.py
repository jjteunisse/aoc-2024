import sys
import numpy as np
from typing import Tuple, Iterator, Set
import time

Position = Tuple[int, int]

def num_cheats(distances:np.ndarray, min_saved:int, radius:int) -> int:
    return np.sum((np.triu(distances, k=min_saved+radius) == radius))

def main(name:str="input"):
    path = "inputs/day20/"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    position = next(zip(*np.where(data == "S")))
    path = [position]
    while True:
        i, j = position
        position = {position for position in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if data[position] != '#' and not position in path}.pop()
        path.append(position)
        if data[position] == 'E':
            break
    
    min_saved = 100
    
    #Task 1
    start = time.time()
    distances = np.sum(np.absolute(np.array(path)[:, np.newaxis] - np.array(path)[np.newaxis]), axis=2)
    print("Number of cheats that save at least {} picoseconds:".format(min_saved), num_cheats(distances, min_saved, 2))
    end = time.time()
    print("Runtime:", end-start)
    
    #Task 2
    start = time.time()
    print("Number of cheats that save at least {} picoseconds:".format(min_saved), 
          sum([num_cheats(distances, min_saved, radius) for radius in range(2, 21)]))
    end = time.time()
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())