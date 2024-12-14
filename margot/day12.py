import sys
import numpy as np
from typing import Tuple, Dict, Set, List
import time
from itertools import cycle
        
Position = Tuple[int, int]
Region = Set[Position]

def neighbours(position:Position) -> List[Position]:
    i, j = position
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    
def perimeter(region:Region):
    return sum([neighbour in region for pos in region for neighbour in neighbours(pos)])

def num_corners(pos:Position, region:Region):
    i, j = pos
    north = (i-1, j) in region
    south = (i+1, j) in region
    west = (i, j-1) in region
    east = (i, j+1) in region
    ne = (i-1, j+1) in region
    nw = (i-1, j-1) in region
    se = (i+1, j+1) in region
    sw = (i+1, j-1) in region
    directions = cycle([north, ne, east, se, south, sw, west, nw])
    
    count = 0
    #north, east, south, west are cardinal directions, those in between are called ordinal.
    cardinal1 = next(directions)
    for _ in range(4):
        ordinal = next(directions)
        cardinal2 = next(directions)
        count += (not ordinal and not (cardinal1^cardinal2)) or (ordinal and not (cardinal1 or cardinal2))
        cardinal1 = cardinal2
    
    return count
    

def count_edges(region:Region) -> int:
    #Though the task asks for the number of edges, I'm really counting the number of corners which is the same.
    return sum([num_corners(pos, region) for pos in region])

def map_regions(data:np.ndarray) -> Dict[int, Set[Position]]:
    plant_regions = {}
    mapping = {}
    no = 0
    for plant in np.unique(data):
        mask = (data == plant)
        plant_region = set(zip(*np.where(mask)))
        queue = {plant_region.pop()}
        while True:
            #Explore region
            mapping[no] = set()
            while any(queue):
                (i, j) = queue.pop()
                queue.update({position for position in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if position in plant_region})
                mapping[no].add((i, j))
                plant_region -= {(i, j)}
            no += 1

            #If all plots for given plant have been mapped, continue to the next plant, else initiate a new region.
            if any(plant_region):
                queue = {plant_region.pop()}
            else:
                break
        
    return mapping

def main():
    start = time.time()
    path = "inputs/day12/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    region_mapping = map_regions(data)
    
    end = time.time()
    
    print("Runtime for data readout:", end-start)
    
    #Task 1
    start = time.time()
    fencing_price = sum([perimeter(region)*len(region) for region in region_mapping.values()])
    end = time.time()
    print("Total price of fencing:", fencing_price)
    print("Runtime for task 1:", end-start)

    #Task 2
    start = time.time()
    fencing_price = sum([count_edges(region)*len(region) for region in region_mapping.values()])
    end = time.time()
    print("Total price of fencing w/ bulk discount:", fencing_price)
    print("Runtime for task 2:", end-start)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())