import sys
import re

def main(name:str="input"):
    path = "inputs/day19/"
    
    with open(path+name+".txt") as file:
        towels = next(file).replace(" ", "").split(",")
        next(file)
        designs = [line.strip() for line in file]
        
    #(Task 1) This much is just using regex... now to wait for the catch.
    pattern = re.compile("({})*".format("("+")|(".join(towels)+")"))
    
    print("Number of possible designs:", sum([pattern.fullmatch(design) != None for design in designs]))
    
    return

if __name__ == "__main__":
    sys.exit(main())