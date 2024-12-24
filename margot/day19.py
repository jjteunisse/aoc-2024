import sys
import re
from typing import List

def count_all_matches(design:str, towels:List[str]):
    matches_per_length = {length:(0 if length != 0 else 1) for length in range(len(design)+1)}
    for length in matches_per_length:
        if matches_per_length[length] == 0:
            continue
            
        for towel in towels:
            if re.match(towel, design[length:]):
                matches_per_length[length+len(towel)] += matches_per_length[length]
                
    return matches_per_length[len(design)]
        

def main(name:str="input"):
    path = "inputs/day19/"
    
    with open(path+name+".txt") as file:
        towels = next(file).strip().replace(" ", "").split(",")
        next(file)
        designs = [line.strip() for line in file]
    
    #(Task 1) This much is just using regex... now to wait for the catch.
    pattern = re.compile("^({})*$".format("("+")|(".join(towels)+")"))
    possible_designs = [design for design in designs if pattern.match(design) != None]
    
    print("Number of possible designs:", len(possible_designs))
    
    #(Task 2) Getting flashbacks to day 12 last year... but already went through that, so.
    print("All matches:", sum([count_all_matches(design, towels) for design in possible_designs]))
    
    return

if __name__ == "__main__":
    sys.exit(main())