import sys
import numpy as np

def main():
    path = "inputs/day9/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array(list(next(file).strip()), dtype=int)
    
    files = data[::2]
    free = data[1::2]
    
    #(Task 1) Probably not very efficient, but I'll start by doing this the way it was shown in the task.
    blocks = []
    for i in range(len(free)):
        blocks += [i]*files[i]
        blocks += [None]*free[i]
    blocks += [len(files)-1]*files[-1]
    blocks = np.array(blocks)
    
    free_space = (blocks == None)
    blocks[free_space] = blocks[blocks != None][:-sum(free_space)-1:-1]
    blocks = blocks[:-sum(free_space)]
    
    print("Checksum:", np.sum(blocks*np.arange(len(blocks))))
    
    return

if __name__ == "__main__":
    sys.exit(main())