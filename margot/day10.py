import sys
import numpy as np

def main():
    path = "inputs/day10/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file], dtype=int)
        
    height_map = {height:set(zip(*np.where(data == height))) for height in range(10)}
    
    total_score = 0
    for trailhead in height_map[0]:
        queue = set()
        queue.add(trailhead)
        for height in range(1, 10):
            queue_new = set()
            for source in queue:
                i, j = source
                queue_new.update({target for target in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if target in height_map[height]})
            queue = queue_new
        total_score += len(queue)
    print("Total score:", total_score)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())