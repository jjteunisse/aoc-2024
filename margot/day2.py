import sys
import numpy as np

def main():
    path = "inputs/day2/"
    name = "input"
    
    data = [np.array(line.split(), dtype=int) for line in open(path+name+".txt")]
    
    #Task 1
    diffs = [np.diff(row) for row in data]
    safe = [np.all((rowdiff >= -3)*(rowdiff <= -1)) or np.all((rowdiff >= 1)*(rowdiff <= 3)) for rowdiff in diffs]
    print("Number of safe reports:", np.sum(safe))
    
    #Task 2
    diffs_one_removed = [np.diff([list(row[:i]) + list(row[i+1:]) for i in range(len(row))], axis=1) for row in data]
    safe_one_removed = [np.any(np.all((planediff >= -3)*(planediff <= -1), axis=1)) or  np.any(np.all((planediff >= 1)*(planediff <= 3), axis=1)) for planediff in diffs_one_removed]
    print("Number of safe reports when allowing for one removal:", np.sum(np.logical_or(safe, safe_one_removed)))
    
    return

if __name__ == "__main__":
    sys.exit(main())