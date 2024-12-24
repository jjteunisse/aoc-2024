import sys
import time

def main(name:str="input", gridsize:int=71, task1_limit:int=1024, show=False):
    path = "inputs/day18/"
    
    with open(path+name+".txt") as file:
        data = [tuple(int(i) for i in line.strip().split(",")) for line in file]
    
    #Task 1
    start = time.time()
    
    #Worth implementing Dijkstra's without NetworkX for once.
    shortest_path = {(x, y):float('inf') for x in range(gridsize) for y in range(gridsize) if not (x, y) in data[:task1_limit]}
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
    
    #Show grid
    if show:
        for x in range(gridsize):
            print("".join([('X' if (x, y) == (28, 9) else '#' if (x, y) in data[:task1_limit] else '.') for y in range(gridsize)]))
    
    #Task 2
    start = time.time()
    #Reachability from (0, 0); initialize at the value where the position itself is corrupted. This gives an overestimation.
    until_corrupted = {(x,y):data.index((x, y)) if (x, y) in data else float('inf') for x in range(gridsize) for y in range(gridsize)}
    until_unreachable = {(x, y):-1 for x in range(gridsize) for y in range(gridsize)}
    
    queue = {(0, 0)}
    until_unreachable[(0, 0)] = until_corrupted[(0, 0)]
    while queue:
        (x, y) = queue.pop()
        if x > 0 and until_unreachable[(x, y)] > until_unreachable[(x-1, y)]:
            if until_unreachable[(x-1, y)] < until_corrupted[(x-1, y)]:
                if until_unreachable[(x, y)] >= until_corrupted[(x-1, y)]:
                        until_unreachable[(x-1, y)] = until_corrupted[(x-1, y)]
                else:
                    until_unreachable[(x-1, y)] = until_unreachable[(x, y)]
                queue.add((x-1, y))
        
        if y > 0 and until_unreachable[(x, y)] > until_unreachable[(x, y-1)]:
            if until_unreachable[(x, y-1)] < until_corrupted[(x, y-1)]:
                if until_unreachable[(x, y)] >= until_corrupted[(x, y-1)]:
                        until_unreachable[(x, y-1)] = until_corrupted[(x, y-1)]
                else:
                    until_unreachable[(x, y-1)] = until_unreachable[(x, y)]
                queue.add((x, y-1))

            
        if x < gridsize-1 and until_unreachable[(x, y)] > until_unreachable[(x+1, y)]:
            if until_unreachable[(x+1, y)] < until_corrupted[(x+1, y)]:
                if until_unreachable[(x, y)] >= until_corrupted[(x+1, y)]:
                        until_unreachable[(x+1, y)] = until_corrupted[(x+1, y)]
                else:
                    until_unreachable[(x+1, y)] = until_unreachable[(x, y)]
                queue.add((x+1, y))


        if y < gridsize-1 and until_unreachable[(x, y)] > until_unreachable[(x, y+1)]:
            if until_unreachable[(x, y+1)] < until_corrupted[(x, y+1)]:
                if until_unreachable[(x, y)] >= until_corrupted[(x, y+1)]:
                        until_unreachable[(x, y+1)] = until_corrupted[(x, y+1)]
                else:
                    until_unreachable[(x, y+1)] = until_unreachable[(x, y)]
                queue.add((x, y+1))
    
    end = time.time()
    print("First byte that makes bottom-right corner unreachable:", ",".join([str(i) for i in data[until_unreachable[gridsize-1, gridsize-1]]]))
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    main(task1_limit=994)
    sys.exit()