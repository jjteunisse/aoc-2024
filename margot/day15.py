import sys
import numpy as np
from typing import Set, Tuple, Iterator, Sequence, List, Dict
from abc import ABC, abstractmethod, abstractproperty
import time

Position = Tuple[int, int]
Direction = Tuple[int, int]
    
def task1(instructions:List[Direction], robot:Position, boxes:Set[Position], walls:Set[Position]) -> Tuple[Position, Set[Position]]:
    for direction in instructions:
        robot = (robot[0]+direction[0], robot[1]+direction[1])
        position = robot
        while position in boxes:
             position = (position[0]+direction[0], position[1]+direction[1])
        
        if position in walls:
            robot = (robot[0]-direction[0], robot[1]-direction[1])
        elif robot in boxes:
            boxes.remove(robot)
            boxes.add(position)
            
    return robot, boxes

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
    
    #(Task 1) Movement on a grid again. Oh dear.
    boxsize = 1
    walls = set(zip(*np.where(data == "#")))
    boxes = set(zip(*np.where(data == "O")))
    robot = next(zip(*np.where(data == "@")))

    robot, boxes = task1(instructions, robot, boxes, walls)
    
    print("Sum of GPS coordinates:", sum([100*i + j for (i, j) in boxes]))
    end = time.time()
    print("Runtime:", end-start)
    
    #Task 2
    
    return

if __name__ == "__main__":
    sys.exit(main())