import sys
import numpy as np
from typing import Set, Tuple, Iterator, Sequence, List, Dict
from abc import ABC, abstractmethod, abstractproperty
import time

Position = Tuple[int, int]
Direction = Tuple[int, int]

class Robot:
    direction:(0, 0)
    
    def __init__(self, position:Position) -> None:
        self.position = position

    def push(self, direction:Direction) -> None:
        self.position = (self.position[0]+direction[0], self.position[1]+direction[1])
        self.direction = direction

class Warehouse:
    def __init__(self, robot:Robot, boxes:Dict[Position, Direction], walls:Set[Position]) -> None:
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
        position = self.robot.position
        while position in self.boxes:
            position = (position[0]+direction[0], position[1]+direction[1])
        
        if position in self.walls:
            self.robot.push((-direction[0], -direction[1]))
        elif self.robot.position in self.boxes:
            self.boxes.remove(self.robot.position)
            self.boxes.add(position)
            

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
        
    
    start = time.time()
    
    #Movement on a grid again. Oh dear.
    walls = set(zip(*np.where(data == "#")))
    boxes = set(zip(*np.where(data == "O")))
    robot = Robot(next(zip(*np.where(data == "@"))))

    warehouse = Warehouse(robot, boxes, walls)
    warehouse.simulate(instructions)
    
    print("Sum of GPS coordinates:", sum([100*i + j for (i, j) in warehouse.boxes]))
    end = time.time()
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())