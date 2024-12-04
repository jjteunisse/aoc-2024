import sys
import numpy as np
import re
import multiprocessing as mp
import time

def check_xmas(row:np.ndarray) -> bool:
    count = 0
    line = "".join(row)
    for match in re.finditer("XMAS", line):
        count += 1
    line_reversed = "".join(row[::-1])
    for match in re.finditer("XMAS", line_reversed):
        count += 1
    return count

def check_crossmas(square:np.ndarray) -> bool:
    diag1 = "".join(np.diag(square, 0))
    diag2 = "".join(np.diag(square[:, ::-1], 0))
    return (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM")

def main():
    path = "inputs/day4/"
    name = "input"
    
    start = time.time()
    data = np.array([tuple(line.strip()) for line in open(path+name+".txt")])
    
    #Task 1
    count = 0
    for row in data:
         count += check_xmas(row)
    for col in data.T:
         count += check_xmas(row)
    for i in range(-data.shape[0], data.shape[1]):
         diag1 = np.diagonal(data, i)
         count += check_xmas(diag1)
         diag2 = np.diagonal(data[:,::-1], i)
         count += check_xmas(diag2)
    end = time.time()
    print("Number of XMAS matches:", count)
    print("Runtime", end-start)
    
    #Task 2
    start = time.time()
    iterator = (data[i:i+3, j:j+3] for i, j in np.ndindex(data.shape[0]-2, data.shape[1]-2))
    with mp.Pool() as pool:
        count = sum(pool.map_async(check_crossmas, iterator).get())
    end = time.time()
    print("Number of cross-MAS matches:", count)
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())