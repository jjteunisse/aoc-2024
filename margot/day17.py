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
            combo[4] //= 2**combo[operand]
        elif opcode == 1:
            combo[5] ^= operand
        elif opcode == 2:
            combo[5] = combo[operand]%8
        elif opcode == 3:
            if combo[4] != 0:
                pointer = operand
                continue
        elif opcode == 4:
            combo[5] ^= combo[6]
        elif opcode == 5:
            outputs.append(str(combo[operand]%8))
        elif opcode == 6:
            combo[5] = combo[4]//2**combo[operand]
        elif opcode == 7:
            combo[6] = combo[4]//2**combo[operand]
        else:
            raise Exception("Invalid opcode.")
            
        pointer += 2
        
    return ",".join(outputs)
    
def task2(program:List[int], outputs:List[int]) -> int:
    """
    I'm going to go through the opcodes/operands found in the specific input - not sure it's even possible to solve this generically.
    Just for convenience, the operations carried out in this specific input are:
    1. B = A % 8
    2. B ^= 1 (note XOR is its own inverse)
    3. C = A//2**B
    4. B ^= 5
    5. B ^= C
    6. output = B % 8
    7. If A=0 terminate program, otherwise return to 1.
    """
    
    #First, initialize A at 0. 
    A_allowed = {0}
    for output in outputs[::-1]:
        A_allowed_new = set()
        for A in A_allowed:
            #The values of A and C are restricted by the fact that B needs to be a 3-bit number at a certain point.
            C_allowed = [(A*8+B^1)//2**B for B in range(8)]
            #Now that I have my list of allowed values, I just need to check which of my chosen B's  match the target output.
            A_allowed_new.update({A*8+B^1 for B, C in zip(range(8), C_allowed) if ((B^5)^C)%8 == output})
        A_allowed = A_allowed_new
    
    return min(A_allowed)
        

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
    
    #(Task 2) This works for any target output, but only for the specific program given.
    if name == "input":
        start = time.time()
        print("Lowest possible A that will give program itself as output:", task2(program, program))
        end = time.time()
    else:
        print("Can only do part 2 for the program given in the task.")
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())