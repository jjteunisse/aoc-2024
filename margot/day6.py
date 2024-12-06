import sys
from typing import Tuple
import numpy as np

Position = Tuple[int]
Direction  = Tuple[int]

class Guard():
    def __init__(self, starting_position:Position, starting_direction:Direction):
        self.position = starting_position
        if starting_direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            self.direction = starting_direction
        else:
            raise Exception("Invalid direction.")
        
    def update(self, rocks:np.ndarray) -> Position:
        i = self.position[0] + self.direction[0]
        j = self.position[1] + self.direction[1]
        if (i == -1 or j == -1) or (i == rocks.shape[0] or j == rocks.shape[1]):
            raise Exception("Guard has left the area.")
        
        if rocks[i, j]:
            self.direction = (self.direction[1], -self.direction[0])
        else:
            self.position = (i, j)
        return (self.position, self.direction)

def main():
    path = "inputs/day6/"
    name = "test"
    
    data = np.array([list(line.strip()) for line in open(path+name+".txt")])
    rocks = (data == "#")
    guard_position = tuple(x[0] for x in np.where((data != "#")*(data != ".")))
    direction_mapping = {">":(0, 1), "<":(0, -1), "^":(0, -1), "v":(0, 1)}
    guard_direction = direction_mapping[data[guard_position]]
    
    guard = Guard(guard_position, guard_direction)
    
    visited = {(guard_position, guard_direction)}
    visited_positions = {guard_position}
    loop = False
    while not loop:
        try:
            position, direction = guard.update(rocks)
            if (position, direction) in visited:
                loop = True
            else:
                visited.add((position, direction))
                visited_positions.add(position)
        except Exception as exception:
            print(exception)
            break
    print("Number of visited positions:", len(visited_positions))
    
    return

if __name__ == "__main__":
    sys.exit(main())