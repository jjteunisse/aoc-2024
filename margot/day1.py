import numpy as np
import sys

def main():
    #Read data
    path = "inputs/day1/"
    name = "input"
    
    data = np.array([line.split() for line in open(path+name+".txt")], dtype=int)

    #Part 1
    print("Total distance:", np.sum(np.absolute(np.diff(np.sort(data, axis=0), axis=1)), axis=0)[0])
    
    #Part 2
    counts = {i:count for i, count in zip(*np.unique(data[:, 1], return_counts = True))}
    print("Similarity score:", sum([i*counts[i] if i in counts else 0 for i in data[:, 0]]))
    
    return
    
if __name__ == "__main__":
    sys.exit(main())