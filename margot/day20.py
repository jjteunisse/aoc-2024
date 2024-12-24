import sys
import numpy as np
from typing import Tuple, Iterator, Set
import time

Position = Tuple[int, int]

def next_nearest(position:Position) -> Set[Position]:
    i, j = position
    return {(i+2, j), (i+1, j+1), (i, j+2), (i-1, j+1), (i-2, j), (i-1, j-1), (i, j-2), (i+1, j-1)}

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
    
    #Task 1
    start = time.time()
    min_saved = 100
    
    num_cheats = sum([len(next_nearest(source).intersection(set(path[index+min_saved+2:])))
              for index, source in enumerate(path[:-min_saved-2])])
    
    end = time.time()
    
    print("Number of cheats that save at least {} picoseconds:".format(min_saved), num_cheats)
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())