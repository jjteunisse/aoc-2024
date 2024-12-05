import sys
from typing import Tuple, Set

Pages=Tuple[int]
Order=Set[Tuple[int]]

def check_sorted(pages:Pages, order:Order) -> bool:
    for i in range(len(pages)):
        num1 = pages[i]
        if any({(num2, num1) in order for num2 in pages[i+1:]}):
            return False
    return True
    
def sort(pages:Pages, order:Order)-> Pages:
    i = 0
    while i < len(pages):
        num1 = pages[i]
        mismatch = False
        for num2 in pages[i+1:]:
            if (num2, num1) in order:
                #If num1, num2 are sorted incorrectly, move num2 right before num1
                pages = pages[:i] + (num2,) + pages[i:pages.index(num2)] + pages[pages.index(num2)+1:]
                mismatch = True
                break
        if not mismatch:
            i += 1
    return pages

def main():
    path = "inputs/day5/"
    name = "input"
    
    order = set()
    count_correct = 0
    count_incorrect = 0
    with open(path+name+".txt") as file:
        for line in file:
            if line == "\n":
                break
            num1, num2 = line.split("|")
            order.add((int(num1), int(num2)))
            
        for line in file:
            pages = tuple(int(num) for num in line.split(","))
            if check_sorted(pages, order):
                count_correct += pages[len(pages)//2]
            else:
                pages = sort(pages, order)
                count_incorrect += pages[len(pages)//2]
            
    print("Sum of middle numbers for initially sorted updates:", count_correct)
    print("Sum of middle numbers for initially unsorted updates:", count_incorrect)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())