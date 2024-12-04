import sys
import numpy as np
import re
import time

def main():
    path = "inputs/day4/"
    name = "input"
    
    start = time.time()
    data = np.array([tuple(line.strip()) for line in open(path+name+".txt")])
    
    iterator = np.array([row for row in data] + [col for col in data.T] + [np.diagonal(data, i) for i in range(-data.shape[0], data.shape[1])] + [np.diagonal(data[:,::-1], i) for i in range(-data.shape[0], data.shape[1])], dtype=object)
    
    count = 0
    for row in iterator:
        line = "".join(row)
        for match in re.finditer("XMAS", line):
            count += 1
        line_reversed = "".join(row[::-1])
        for match in re.finditer("XMAS", line_reversed):
            count += 1
        
    end = time.time()
    print("Number of XMAS matches:", count)
    print("Runtime", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())