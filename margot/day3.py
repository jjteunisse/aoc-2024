import sys
import re

def main():
    path = "inputs/day3/"
    name = "input"
    
    #Task 1. Not sure if I should consider lines separately or combine them, but since the given input has lines all ending in mul(...,...) this isn't a problem.
    pattern = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    
    with open(path+name+".txt") as file:
        print("Sum of multiplications:", sum([int(match.groups()[0])*int(match.groups()[1]) for line in file for match in pattern.finditer(line)]))
    
    #Task 2
    pattern_with_disabling = re.compile("(mul\(\d{1,3},\d{1,3}\)|don't|do)")
    
    count = 0
    enabled = True
    file = open(path+name+".txt")
    for line in file:
        for match in pattern_with_disabling.finditer(line):
            output = match.groups()[0]
            if output == "don't":
                enabled = False
            elif output == "do":
                enabled = True
            elif enabled:
                int1, int2= pattern.match(output).groups()
                count += int(int1)*int(int2)
    file.close()
    print("Enabled only:", count)
    
    return

if __name__ == "__main__":
    sys.exit(main())