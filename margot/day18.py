import sys
import time

def main(name:str, gridsize:int, task1_limit:int):
    path = "inputs/day18/"
    
    with open(path+name+".txt") as file:
        data = [tuple(int(i) for i in line.strip().split(",")[::-1]) for line in file]
    
    #Task 1
    start = time.time()
    
    #Worth implementing Dijkstra's without NetworkX for once.
    corrupted = set(data[:task1_limit])
    shortest_path = {(x, y):float('inf') for x in range(gridsize) for y in range(gridsize) if not (x, y) in corrupted}
    target = (gridsize-1, gridsize-1)
    
    num_steps = 0
    queue = {(0, 0)}
    while not target in queue:
        for position in queue:
            shortest_path.pop(position)
        
        for (x, y) in queue:
            for position in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if position in shortest_path:
                    shortest_path[position] = num_steps+1
        
        num_steps = min(shortest_path.values())
        queue = {position for position in shortest_path if shortest_path[position] == num_steps}
    
    end = time.time()
    
    print("Shortest path length after {} bytes have fallen:".format(task1_limit), shortest_path[target])
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    #Run test input
    main("test", gridsize=7, task1_limit=12)
    #Run target input
    main("input", gridsize=71, task1_limit=1024)
    sys.exit()