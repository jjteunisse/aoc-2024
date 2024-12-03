import sys
import re

def main():
    path = "inputs/day3/"
    name = "input"
    
    line = next(open(path+name+".txt"))
    
    pattern = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    
    #Task 1
    print("Sum of multiplications:", sum([int(match.groups()[0])*int(match.groups()[1]) for match in pattern.finditer(line)]))
    
    return

if __name__ == "__main__":
    sys.exit(main())