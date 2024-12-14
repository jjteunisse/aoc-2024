import sys
import re
from typing import Tuple, List, Iterator
import numpy as np

Position = Tuple[int, int]
Velocity = Tuple[int, int]

class RobotSimulation():
    #This is a bit like a molecular dynamics simulation isn't it? 
    def __init__(self, width:int, height:int, positions:List[Position], velocities:List[Velocity]) -> None:
        self.width = width
        self.height = height
        self.positions = np.array(positions)
        self.velocities = np.array(velocities)
        
    def update(self, seconds:int) -> None:
        self.positions[:, 0] = (self.positions[:, 0] + seconds*self.velocities[:, 0])%self.height
        self.positions[:, 1] = (self.positions[:, 1] + seconds*self.velocities[:, 1])%self.width
        
def safety_factor(robsim:RobotSimulation) -> int:
    first = sum([(i < robsim.height//2 and j < robsim.width//2) for (i, j) in robsim.positions])
    second = sum([(i < robsim.height//2 and j > robsim.width//2) for (i, j) in robsim.positions])
    third = sum([(i > robsim.height//2 and j < robsim.width//2) for (i, j) in robsim.positions])
    fourth = sum([(i > robsim.height//2 and j > robsim.width//2) for (i, j) in robsim.positions])
    
    return first*second*third*fourth

def main(name:str, width:int, height:int, seconds:int):
    path = "inputs/day14/"
    
    pattern = re.compile("p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)")
    positions = []
    velocities = []
    with open(path+name+".txt") as file:
        for line in file:
            groups = pattern.match(line).groups()
            positions.append((int(groups[1]), int(groups[0])))
            velocities.append((int(groups[3]), int(groups[2])))
            
    #Task 1
    robsim = RobotSimulation(width, height, positions, velocities)
    robsim.update(seconds)
    
    print("Safety factor:", safety_factor(robsim))
    
    return
    
if __name__ == "__main__":
    #Run test
    main("test", 11, 7, 100)
    #Run for real input
    main("input", 101, 103, 100)
    sys.exit()