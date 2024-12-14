import sys
import re
import numpy as np

def main():
    path = "inputs/day13/"
    name = "input"
    
    button_pattern = re.compile("Button\s[AB]:\sX\+(\d+),\sY\+(\d+)")
    prize_pattern = re.compile("Prize:\sX=(\d+),\sY=(\d+)")
    
    tokens = 0
    tokens_offset = 0
    with open(path+name+".txt") as file:
        while True:
            buttona = tuple(int(num) for num in button_pattern.match(next(file)).groups())
            buttonb = tuple(int(num) for num in button_pattern.match(next(file)).groups())
            prize = tuple(int(num) for num in prize_pattern.match(next(file)).groups())
            
            #This is a system of 2 (independent) linear equations in 2 variables, so there is one solution. 
            #Can also solve manually but numpy is optimized for this, and takes care of checking for dependency.
            matrix = np.array([buttona, buttonb], dtype=np.int64).T
            
            #Task 1
            solA, solB = np.linalg.solve(matrix, prize)
            if (solA > 0 and solB > 0) and np.isclose(solA, np.round(solA)) and np.isclose(solB, np.round(solB)):
                tokens += int(np.round(3*solA + solB))
                
            #(Task 2) sneaky floating point errors... 
            offset = 10000000000000
            solA, solB = np.linalg.solve(matrix, (prize[0]+offset, prize[1]+offset))
            if (solA > 0 and solB > 0) and np.isclose(solA, np.round(solA), rtol=1/float(offset)) and np.isclose(solB, np.round(solB), rtol=1/float(offset)):
                tokens_offset += int(np.round(3*solA + solB))
            
            try:
                next(file)
            except StopIteration:
                break
        
    print("Number of tokens needed:", tokens)
    print("Number of tokens needed with offset:", tokens_offset)
        
    return

if __name__ == "__main__":
    sys.exit(main())