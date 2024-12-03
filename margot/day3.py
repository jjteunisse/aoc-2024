import sys
import re

def main():
    path = "inputs/day3/"
    name = "input"
    
    pattern = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    
    #Task 1. Not sure if I should consider lines separately or combine them, but since the given input has lines all ending in mul(...,...) this isn't a problem.
    print("Sum of multiplications:", sum([int(match.groups()[0])*int(match.groups()[1]) for line in open(path+name+".txt") for match in pattern.finditer(line)]))
    
    return

if __name__ == "__main__":
    sys.exit(main())