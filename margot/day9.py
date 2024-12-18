import sys
import numpy as np
import time

def main():
    path = "inputs/day9/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = [int(i) for i in next(file).strip()]
    
    files = data[::2]
    free = data[1::2]
    
    #(Task 1) Probably not very efficient, but I'll start by doing this the way it was shown in the task.
    start = time.time()
    
    blocks = []
    for i in range(len(free)):
        blocks += [i]*files[i]
        blocks += [None]*free[i]
    blocks += [len(files)-1]*files[-1]
    
    #Here I'm using numpy b/c I need to do masking. 
    blocks = np.array(blocks)
    free_blocks = (blocks == None)
    blocks[free_blocks] = blocks[blocks != None][:-sum(free_blocks)-1:-1]
    blocks = blocks[:-sum(free_blocks)]
    
    end = time.time()
    
    print("Checksum:", np.sum(blocks*np.arange(len(blocks))))
    print("Runtime:", end-start)
    
    #(Task 2) This seems easier to optimize since the files don't need to be split up - although it's significantly slower than task 1 in my execution.
    start = time.time()
    
    checksum = 0
    file_positions = np.cumsum([[0]+[files[i]+free[i] for i in range(len(free))]], dtype=np.int64)
    free_positions = np.cumsum([files[0]]+[files[i+1]+free[i] for i in range(len(free))], dtype=np.int64)
    filled = [0]*len(free)
    for i in range(len(files)-1, -1, -1):
        moved = False
        for j in range(i):
            if files[i] <= free[j]-filled[j]:
                starting_position = free_positions[j] + filled[j]
                checksum += np.sum(i*np.arange(starting_position, starting_position+files[i]), dtype=np.int64)
                filled[j] += files[i]
                moved = True
                break
        if not moved:
            checksum += np.sum(i*np.arange(file_positions[i], file_positions[i]+files[i]), dtype=np.int64)
            
    end = time.time()
        
    print("Checksum for whole file movement:", checksum)
    print("Runtime:", end-start)
        
    return

if __name__ == "__main__":
    sys.exit(main())