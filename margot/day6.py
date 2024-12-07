import sys
from typing import Tuple, Iterator
import numpy as np
import time
import multiprocessing as mp

Position = Tuple[int]
Direction  = Tuple[int]

class Guard():
    def __init__(self, starting_position:Position, starting_direction:Direction):
        self.position = starting_position
        if starting_direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            self.direction = starting_direction
        else:
            raise Exception("Invalid direction.")
        self.history = []
        
    def turn(self) -> Direction:
        self.direction = (self.direction[1], -self.direction[0])
        
    def update(self, rocks:np.ndarray) -> Tuple[Position, Direction]:
        self.history.append((self.position, self.direction))
        i = self.position[0] + self.direction[0]
        j = self.position[1] + self.direction[1]
        if (i == -1 or j == -1) or (i == rocks.shape[0] or j == rocks.shape[1]):
            raise Exception("Guard has left the area.")
        
        if rocks[i, j]:
            self.turn()
        else:
            self.position = (i, j)
        
        return (self.position, self.direction)
        
    def walk(self, rocks:np.ndarray) -> bool:
        #Walk until either a loop is reached or the guard leaves the area.
        while True:
            try:
                if (self.position, self.direction) in self.history:
                    return True
                
                self.update(rocks)
                
            except Exception as exception:
                return False
                
    def quickwalk(self, rocks:np.ndarray) -> bool:
        while True:
            try:
                position, direction = self.position, self.direction
                if (position, direction) in self.history:
                    return True
                else:
                    self.history.append((position, direction))
                
                i, j = position
                if direction[0] == 0:
                    line_of_sight = list(rocks[i, j+direction[1]::direction[1]])
                    if any(line_of_sight):
                        j += direction[1]*line_of_sight.index(True)
                    else:
                        raise Exception("Guard has left the area.")
                else:
                    line_of_sight = list(rocks[i+direction[0]::direction[0], j])
                    if any(line_of_sight):
                        i += direction[0]*line_of_sight.index(True)
                    else:
                        raise Exception("Guard has left the area.")

                self.position = (i, j)
                self.turn()
                
            except Exception as exception:
                return False
       
def main():
    path = "inputs/day6/"
    name = "input"
    
    data = np.array([list(line.strip()) for line in open(path+name+".txt")])
    rocks = (data == "#")
    guard_position = tuple(x[0] for x in np.where((data != "#")*(data != ".")))
    direction_mapping = {">":(0, 1), "<":(0, -1), "^":(-1, 0), "v":(1, 0)}
    guard_direction = direction_mapping[data[guard_position]]
    
    #Task 1
    start = time.time()
    guard = Guard(guard_position, guard_direction)
    
    guard.walk(rocks)
    visited = {position for (position, direction) in guard.history}
        
    end = time.time()

    print("Number of visited positions:", len(visited))
    print("Runtime:", end-start)
    
    #Task 2
    start = time.time()
    
    rock_positions = set()
    guard_positions = [position for (position, direction) in guard.history]
    
    for no, (position, direction) in enumerate(guard.history[:-1]):
        
        i = position[0] + direction[0]
        j = position[1] + direction[1]
        
        #There must not already be a rock in place, and the rock cannot cross the preceding path of the guard.
        if rocks[i, j] or (i, j) in guard_positions[:no]:
            continue
            
        rocks_plus_one = rocks.copy()
        rocks_plus_one[i, j] = True
            
        ghost = Guard(position, direction)
        ghost.turn()

        loop = ghost.quickwalk(rocks_plus_one)
        if loop:
            rock_positions.add((i, j))
    
    end = time.time()
    
    print("Number of possible rock positions:", len(rock_positions))
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())