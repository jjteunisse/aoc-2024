import sys
import numpy as np
import re

def main():
    path = "inputs/day4/"
    name = "test"
    
    data = np.array([tuple(line.strip()) for line in open(path+name+".txt")])
    print(data)
    
    iterator = [row for row in data] + [row for row in data[:, ::-1]] + [col for col in data.T] + [col for col in data[::-1].T]
    
    count = 0
    for row in iterator:
        line = "".join(row)
        for match in re.finditer("XMAS", line):
            count += 1
        
    print("Number of XMAS matches:", count)
    
    return

if __name__ == "__main__":
    sys.exit(main())