import sys
import itertools
from typing import Tuple

def main():
    path = "inputs/day7/"
    name = "input"
    
    count = 0
    for line in open(path+name+".txt"):
        groups = line.strip().split(":")
        test_val = int(groups[0])
        calibration_vals = tuple(int(val) for val in groups[1].split())
        
        queue = {calibration_vals[0]}
        for val2 in calibration_vals[1:]:
            queue_new = {val1+val2 for val1 in queue}
            queue_new.update({val1*val2 for val1 in queue})
            queue = queue_new
            
        count += test_val*any([val == test_val for val in queue])
        
    print("Total calibration result:", count)
        
    return
    
if __name__ == "__main__":
    sys.exit(main())