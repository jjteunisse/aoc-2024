import sys
from typing import Tuple, Iterator, List
import numpy as np
import time

Position = Tuple[int, int]
Direction  = Tuple[int, int]
Rocks = np.ndarray

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
        
    def line_of_sight(self, rocks:Rocks) -> List[bool]:
        i, j = self.position
        direction = self.direction
        if direction[0] == 0:
            return list(rocks[i, j+direction[1]::direction[1]])
        else:
            return list(rocks[i+direction[0]::direction[0], j])
        
    def in_front(self) -> Position:
        return (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        
    def step(self, rocks:Rocks) -> Tuple[Position, Direction]:
        self.history.append((self.position, self.direction))
        i, j = self.in_front()
        if (i == -1 or j == -1) or (i == rocks.shape[0] or j == rocks.shape[1]):
            raise Exception("Guard has left the area.")
        
        if rocks[i, j]:
            self.turn()
        else:
            self.position = (i, j)
        
        return (self.position, self.direction)
        
    def quickstep(self, rocks:Rocks) -> Tuple[Position, Direction]:
        position, direction = self.position, self.direction
        self.history.append((position, direction))
                
        i, j = position
        line_of_sight = self.line_of_sight(rocks)
        if any(line_of_sight):
            i += direction[0]*line_of_sight.index(True)
            j += direction[1]*line_of_sight.index(True)
        else:
            raise Exception("Guard has left the area.")

        self.position = (i, j)
        self.turn()
        return (self.position, self.direction)
        
        
    def walk(self, rocks:Rocks, quick:bool=False) -> bool:
        #Walk until either a loop is reached or the guard leaves the area.
        while True:
            try:
                if (self.position, self.direction) in self.history:
                    return True
                
                if quick:
                    self.quickstep(rocks)
                else:
                    self.step(rocks)
                
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
    visited = [position for (position, direction) in guard.history]
        
    end = time.time()

    print("Number of visited positions:", len(set(visited)))
    print("Runtime:", end-start)
    
    #Task 2
    start = time.time()
    
    rock_positions = set()
    
    for no, (position, direction) in enumerate(guard.history[:-1]):
        ghost = Guard(position, direction)
        in_front = ghost.in_front()
        
        #There must not already be a rock in place, and the rock cannot cross the preceding path of the guard.
        if rocks[in_front] or in_front in visited[:no]:
            continue
            
        rocks_plus_one = rocks.copy()
        rocks_plus_one[in_front] = True

        if ghost.walk(rocks_plus_one, quick=True):
            rock_positions.add(in_front)
    
    end = time.time()
    
    print("Number of possible rock positions:", len(rock_positions))
    print("Runtime:", end-start)
    
    return

if __name__ == "__main__":
    sys.exit(main())