import sys
import numpy as np
from typing import Tuple, List

Position = Tuple[int, int]

def neighbours(position:Position) -> List[Position]:
    i, j = position
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def main():
    path = "inputs/day10/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file], dtype=int)
        
    height_map = {height:set(zip(*np.where(data == height))) for height in range(10)}
    
    #Task 1
    total_score = 0
    for trailhead in height_map[0]:
        queue = {trailhead}
        for height in range(1, 10):
            queue = {target for source in queue for target in neighbours(source) if target in height_map[height]})
        total_score += len(queue)
    print("Total score:", total_score)
    
    #(Task 2) yeah no kidding
    trails = {source:1 for source in height_map[0]}
    for height in range(1, 10):
        trails = {target: sum([trails[source] for source in neighbours(target) if source in height_map[height-1]])
                  for target in height_map[height]}
    print("Sum of ratings:", sum(trails.values()))
        
    return
    
if __name__ == "__main__":
    sys.exit(main())