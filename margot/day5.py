import sys
from typing import Tuple, Set

def check_sorted(pages:Tuple[int], order:Set[Tuple[int]]) -> bool:
    for i in range(len(pages)):
        num1 = pages[i]
        if any({(num2, num1) in order for num2 in pages[i+1:]}):
            return False
    return True

def main():
    path = "inputs/day5/"
    name = "input"
    
    order = set()
    count = 0
    with open(path+name+".txt") as file:
        for line in file:
            if line == "\n":
                break
            num1, num2 = line.split("|")
            order.add((int(num1), int(num2)))
            
        for line in file:
            pages = tuple(int(num) for num in line.split(","))
            if check_sorted(pages, order):
                count += pages[len(pages)//2]
            
    print("Sum of middle numbers for correctly sorted updates:", count)
            
if __name__ == "__main__":
    sys.exit(main())