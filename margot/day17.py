import sys
from typing import List, Tuple
import time

def task1(program:List[int], registers:Tuple[int, int, int]) -> str:
    A, B, C = registers
    
    pointer = 0
    outputs = []
    combo = [i for i in range(4)] + [A, B, C]
    while pointer < len(program) - 1:
        opcode, operand = program[pointer:pointer+2]
        
        if opcode == 0:
            A //= 2**combo[operand]
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = combo[operand]%8
        elif opcode == 3:
            if A != 0:
                pointer = operand
                continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            outputs.append(str(combo[operand]%8))
        elif opcode == 6:
            B = A//2**combo[operand]
        elif opcode == 7:
            C = A//2**combo[operand]
        else:
            raise Exception("Invalid opcode.")
        
        combo[4:] = (A, B, C)
        pointer += 2
        
    return ",".join(outputs)

def main():
    path = "inputs/day17/"
    name = "input"
    
    with open(path+name+".txt") as file:
        registers = tuple(int(next(file).split(":")[1]) for _ in range(3))
        next(file)
        program = [int(digit) for digit in next(file).split(":")[1].split(",")]
        
    #Task 1
    start = time.time()
    print("Result from all outputs:", task1(program, registers))
    end = time.time()
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())