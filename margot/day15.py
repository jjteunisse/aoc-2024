import sys
import numpy as np
from typing import Set, Tuple, Iterator, Sequence, List
from abc import ABC, abstractmethod, abstractproperty

Position = Tuple[int, int]
Direction = Tuple[int, int]

class Pushable(ABC):
    direction:Direction
    position:Position
    size:int

    def push(self, direction:Direction) -> None:
        self.position = (self.position[0]+direction[0], self.position[1]+direction[1])
        self.direction = direction

class Box(Pushable):
     direction = None
     
     def __init__(self, position:Position, size:int) -> None:
         self.position  = position
         self.size = size

class Robot(Pushable):
    direction = (0, -1) #start facing north
    size = 1

    def __init__(self, position:Position) -> None:
        self.position = position

class Warehouse:
    def __init__(self, robot:Robot, boxes:Set[Position], walls:Set[Position]) -> None:
        self.robot = robot
        self.boxes = boxes
        self.walls = walls

    def simulate(self, instructions:List[Direction]):
        for direction in instructions:
            self.robot.push(direction)
            self.equilibrate()

    def equilibrate(self):
        allowed = True
        direction = self.robot.direction
        if self.robot.position in self.boxes:
            self.boxes.remove(self.robot.position)
            position = (self.robot.position[0]+direction[0],  self.robot.position[1]+direction[1])
            while position in self.boxes:
                position = (position[0]+direction[0],  position[1]+direction[1])
            if position in self.walls:
                allowed = False
                position = self.robot.position
            self.boxes.add(position)
        
        else:
            allowed = not (self.robot.position in self.walls)
        
        if not allowed:
            self.robot.push((-direction[0], -direction[1]))

def main():
    path = "inputs/day15/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = []
        for line in file:
            if any(line.strip()):
                data.append(list(line))
            else:
                break
        data = np.array(data)
        
        dir_mapping = {"^":(-1, 0), ">":(0, 1), "<":(0, -1), "v":(1, 0)}
        instructions = [dir_mapping[char] for line in file for char in line.strip()]
        
    #Movement on a grid again. Oh dear.
    walls = set(zip(*np.where(data == "#")))
    boxes = set(zip(*np.where(data == "O")))
    robot = Robot(next(zip(*np.where(data == "@"))))

    warehouse = Warehouse(robot, boxes, walls)
    warehouse.simulate(instructions)
    
    print("Sum of GPS coordinates:", sum([100*i + j for (i, j) in warehouse.boxes]))
    
    return

if __name__ == "__main__":
    sys.exit(main())