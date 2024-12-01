import numpy as np
import sys

def main():
    path = "inputs/day1/"
    name = "input"
    
    data = np.array([line.split() for line in open(path+name+".txt")], dtype=int)

    print("Total distance:", np.sum(np.absolute(np.diff(np.sort(data, axis=0), axis=1)), axis=0)[0])
    
    return
    
if __name__ == "__main__":
    sys.exit(main())