import sys
import itertools
from typing import Tuple
import time
import multiprocessing as mp

def read(line:str) -> Tuple[int, Tuple[int]]:
    groups = line.strip().split(":")
    test_val = int(groups[0])
    calibration_vals = tuple(int(val) for val in groups[1].split())
    return test_val, calibration_vals

def calibration_result(line:str) -> int:
    test_val, calibration_vals = read(line)
    
    queue = {calibration_vals[0]}
    for val2 in calibration_vals[1:]:
        queue_new = {val1+val2 for val1 in queue}
        queue_new.update({val1*val2 for val1 in queue})
        queue = queue_new
    return test_val*any([val == test_val for val in queue])

def calibration_result_with_concatenation(line:str) -> int:
    test_val, calibration_vals = read(line)
    
    queue = {calibration_vals[0]}
    for val2 in calibration_vals[1:]:
        queue_new = {val1+val2 for val1 in queue}
        queue_new.update({val1*val2 for val1 in queue})
        queue_new.update({int(str(val1)+str(val2)) for val1 in queue})
        queue = queue_new
    return test_val*any([val == test_val for val in queue])

def main():
    path = "inputs/day7/"
    name = "input"
    
    data = [(int(line.strip().split(":")[0]), tuple(int(val) for val in line.strip().split(":")[1].split())) for line in open(path+name+".txt")]
    
    pool = mp.Pool()
    
    #Task 1
    start = time.time()
    print("Total calibration result:", sum(pool.map_async(calibration_result, open(path+name+".txt")).get()))
    end = time.time()
    print("Runtime:", end-start)
    
    #Task 2
    start = time.time()
    print("Total calibration result with concatenation:", sum(pool.map_async(calibration_result_with_concatenation, open(path+name+".txt")).get()))
    end = time.time()
    print("Runtime:", end-start)
    
    pool.close()
        
    return
    
if __name__ == "__main__":
    sys.exit(main())