import sys
from typing import Sequence, Callable, List

Stone=int

def replace_zero_by_one(stone:Stone) -> List[Stone]:
    if stone == 0:
        return [1]
    return [stone]
    
def split(stone:Stone) -> List[Stone]:
    engraving = str(stone)
    if len(engraving) %2 == 0:
        left = engraving[:len(engraving)//2]
        right = engraving[len(engraving)//2:]
        return [int(left), int(right)]
    return [stone]
    
def multiply(stone:Stone) -> List[Stone]:
    return [stone*2024]

def blink(stone:Stone, rules:Sequence[Callable]) -> List[Stone]:
    for rule in rules:
        output = rule(stone)
        if output != [stone]:
            return output
    return [stone]

def main():
    path = "inputs/day11/"
    name = "input"
    
    with open(path+name+".txt") as file:
        line = next(file)
        data = [int(i) for i in line.split()]
        
    #I suppose I can just make a list of functions? 
    stones = data.copy()
    rules = [replace_zero_by_one, split, multiply]
    
    #(Task 1) Can maybe do this more efficiently by just keeping track of the counts, but let's start by doing this as written.
    num_blinks = 25
    for _ in range(num_blinks):
        stones_new = []
        for stone in stones:
            stones_new += blink(stone, rules)
        stones = stones_new
    print("Number of stones after {} blinks:".format(num_blinks), len(stones))
    
    return
    
if __name__ == "__main__":
    sys.exit(main())