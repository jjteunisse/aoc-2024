import sys
import numpy as np
from typing import Tuple, Iterator, Set
import time

Position = Tuple[int, int]

def neighbourhood(position:Position, radius:int) -> Set[Position]:
    i, j = position
    positions = {(i+x, j+radius-abs(x)) for x in range(-radius, radius+1)}
    positions.update({(i+x, j-radius+abs(x)) for x in range(-radius+1, radius)})
    return positions

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
    
    num_cheats = 0
    for index, source in enumerate(path[:-min_saved-2]):
        num_cheats += len(neighbourhood(source, 2).intersection(set(path[index+min_saved+2:])))

    end = time.time()
    
    print("Number of cheats that save at least {} picoseconds:".format(min_saved), num_cheats)
    print("Runtime:", end-start)
    
    #Task 2
    start = time.time()
    
    num_cheats = 0
    for radius in range(2, 21):
        for index, source in enumerate(path[:-min_saved-radius]):
            num_cheats += len(neighbourhood(source, radius).intersection(set(path[index+min_saved+radius:])))

    end = time.time()
    
    print("Number of cheats that save at least {} picoseconds:".format(min_saved), num_cheats)
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())