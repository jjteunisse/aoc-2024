import sys
import numpy as np
from typing import Set, Tuple, Iterator, Sequence

Position = Tuple[int, int]
Direction = Tuple[int, int]

class Robot:
    direction = (0, -1) #start facing north

    def __init__(self, position:Position) -> None:
        self.position = position
        
    def move(self, direction:Direction) -> None:
        self.position = (self.position[0]+direction[0], self.position[1]+direction[1])
        self.direction = direction

    def push(self, boxes:Set[Position], walls:Set[Position]) -> Set[Position]:
        allowed = True
        direction = self.direction
        if self.position in boxes:
            boxes.remove(self.position)
            position = (self.position[0]+direction[0],  self.position[1]+direction[1])
            while position in boxes:
                position = (position[0]+direction[0],  position[1]+direction[1])
            if position in walls:
                allowed = False
                position = self.position
            boxes.add(position)
        
        else:
            allowed = not (self.position in walls)
        
        if not allowed:
            self.move((-direction[0], -direction[1]))

        return boxes

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
    
    for direction in instructions:
        robot.move(direction)
        boxes = robot.push(boxes, walls)
    
    print("Sum of GPS coordinates:", sum([100*i + j for (i, j) in boxes]))
    
    return

if __name__ == "__main__":
    sys.exit(main())