import sys
from typing import Sequence, Callable, List
import time

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

def main(num_blinks:int):
    path = "inputs/day11/"
    name = "input"
    
    with open(path+name+".txt") as file:
        line = next(file)
        data = [int(i) for i in line.split()]
        
    #Though the exercise specifies that the stones remain in order, this order is not important.
    #Just saving the number of instances of each number keeps the problem from getting crazy, since the same numbers keep repeating.
    stones = {stone:data.count(stone) for stone in set(data)}
    
    #I suppose there's nothing against just making a list of functions.
    rules = [replace_zero_by_one, split, multiply]
    
    start = time.time()
    for _ in range(num_blinks):
        stones_new = {}
        for old_stone in stones:
            for stone in blink(old_stone, rules):
                if stone in stones_new:
                    stones_new[stone] += stones[old_stone]
                else:
                    stones_new[stone] = stones[old_stone]
        stones = stones_new
    end = time.time()
    print("Number of stones after {} blinks:".format(num_blinks), sum(stones.values()))
    print("Runtime:", end-start)
    
    return
    
if __name__ == "__main__":
    #Since the exercise essentially just asks to run the main function twice, only w/ different num_blinks, I'll just do that.
    main(25)
    main(75)
    sys.exit()