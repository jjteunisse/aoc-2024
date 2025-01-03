import sys
import numpy as np
from typing import Set, Tuple, Iterator, Sequence, List, Dict
from abc import ABC, abstractmethod, abstractproperty
import time

Position = Tuple[int, int]
Direction = Tuple[int, int]

def show(image:np.ndarray):
    for row in image:
        print("".join(row))
    print("\n")
    
def task1(instructions:List[Direction], data:np.ndarray) -> int:
    walls = set(zip(*np.where(data == "#")))
    boxes = set(zip(*np.where(data == "O")))
    robot = next(zip(*np.where(data == "@")))
    
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
            
    return sum([100*i + j for (i, j) in boxes])
    
def task2(instructions:List[Direction], data:np.ndarray, show_grid=False) -> int:
    walls = {(i, 2*j) for (i, j) in zip(*np.where(data == "#"))}
    walls.update({(i, 2*j+1) for (i, j) in zip(*np.where(data == "#"))})
    boxes = {(i, 2*j) for (i, j) in zip(*np.where(data == "O"))}
    i, j = next(zip(*np.where(data == "@")))
    robot = (i, 2*j)
    
    image = np.tile('.', (data.shape[0], 2*data.shape[1]))
    mapping = {(0, 1):'>', (0, -1):'<', (1, 0):'v', (-1, 0):'^'}
        
    for position in walls:
        image[position] = '#'
    
    for direction in instructions:
        image[robot] = mapping[direction]
        robot = (robot[0]+direction[0], robot[1]+direction[1])
        queue = {(robot[0], j) for j in range(robot[1]-1, robot[1]+1) if (robot[0], j) in boxes}
        pushed = set()
        allowed = not (robot in walls)
        while allowed and any(queue):
            pushed.update(queue)
            queue_new = set()
            for position in queue:
                i = position[0]+direction[0]
                if any([(i, j) in walls for j in range(position[1]+direction[1], position[1]+direction[1]+2)]):
                    allowed = False
                    break
                queue_new.update({(i, j) for j in range(position[1]+direction[1]-1, position[1]+direction[1]+2) if (i, j) in boxes - pushed})
            queue = queue_new
        
        if not allowed:
            robot = (robot[0]-direction[0], robot[1]-direction[1])
        else:
            for position in pushed:
                boxes -= pushed
                boxes.update({(position[0]+direction[0], position[1]+direction[1]) for position in pushed})
                
        if show_grid:
            image[robot] = '@'
            for position in boxes:
                image[position] = '['
                image[position[0], position[1]+1] = ']'
            show(image)
            image[image != '#'] = '.'
        
    
    return sum([100*i + j for (i, j) in boxes])

def main():
    path = "inputs/day15/"
    name = "test4"
    
    with open(path+name+".txt") as file:
        data = []
        for line in file:
            if any(line.strip()):
                data.append(list(line.strip()))
            else:
                break
        data = np.array(data)
        
        dir_mapping = {"^":(-1, 0), ">":(0, 1), "<":(0, -1), "v":(1, 0)}
        instructions = [dir_mapping[char] for line in file for char in line.strip()]
        
    
    #Task 1
    start = time.time()
    print("Sum of GPS coordinates (task 1):", task1(instructions, data))
    end = time.time()
    print("Runtime:", end-start)
    
    #Task 2
    start = time.time()
    print("Sum of GPS coordinates (task 2):", task2(instructions, data, show_grid=True))
    end = time.time()
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())