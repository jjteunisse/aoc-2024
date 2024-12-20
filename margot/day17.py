import sys
from typing import Union, List, Iterator

class Computer:
    pointer = 0
    
    def __init__(self, A:int, B:int, C:int) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.instructions = {0:self.adv, 1:self.bxl, 2:self.bst, 3:self.jnz, 4:self.bxc, 5:self.out, 6:self.bdv, 7:self.cdv}
        
    def apply(self, opcode:int, operand:int) -> Union[int, None]:
        return self.instructions[opcode](operand)
        
    def run(self, program:List[int]) -> Iterator[int]:
        result = []
        while self.pointer < len(program)-1:
            opcode, operand = program[self.pointer:self.pointer+2]
            
            output = self.apply(opcode, operand)
            if output != None:
                yield output
        
    def combo(self, operand:int) -> int:
        if 0 <= operand < 4: return operand
        elif operand == 4: return self.A
        elif operand == 5: return self.B
        elif operand == 6: return self.C 
        else: raise Exception("Invalid program.")
        
    def adv(self, operand:int) -> None:
        self.A //= 2**self.combo(operand)
        self.pointer += 2
        
    def bxl(self, operand:int) -> None:
        self.B = self.B^operand
        self.pointer += 2
        
    def bst(self, operand:int) -> None:
        self.B = self.combo(operand)%8
        self.pointer += 2
        
    def jnz(self, operand:int) -> None:
        if not self.A == 0:
            self.pointer = operand
        else:
            self.pointer += 2
            
    def bxc(self, operand:int) -> None:
        self.B = self.B^self.C
        self.pointer += 2
        
    def out(self, operand:int) -> int:
        self.pointer += 2
        return self.combo(operand)%8
        
    def bdv(self, operand:int) -> None:
        self.B = self.A // 2**self.combo(operand)
        self.pointer += 2
        
    def cdv(self, operand:int) -> None:
        self.C = self.A // 2**self.combo(operand)
        self.pointer += 2

def main():
    path = "inputs/day17/"
    name = "input"
    
    with open(path+name+".txt") as file:
        A, B, C = (int(next(file).split(":")[1]) for _ in range(3))
        next(file)
        program = [int(digit) for digit in next(file).split(":")[1].split(",")]
        
    computer = Computer(A, B, C)
    print("Result from all outputs:", ",".join([str(digit) for digit in computer.run(program)]))
    
    return

if __name__ == "__main__":
    sys.exit(main())