import sys
import numpy as np
from typing import Tuple, Dict, Set
import time
from itertools import cycle
        
Position = Tuple[int, int]

def num_corners(pos:Position, positions:Set[Position]):
    i, j = pos
    north = (i-1, j) in positions
    south = (i+1, j) in positions
    west = (i, j-1) in positions
    east = (i, j+1) in positions
    ne = (i-1, j+1) in positions
    nw = (i-1, j-1) in positions
    se = (i+1, j+1) in positions
    sw = (i+1, j-1) in positions
    directions = cycle([north, ne, east, se, south, sw, west, nw])
    
    count = 0
    #north, east, south, west are cardinal directions, those in between are called ordinal.
    cardinal1 = next(directions)
    for _ in range(4):
        ordinal = next(directions)
        cardinal2 = next(directions)
        count += not ordinal and not (cardinal1^cardinal2)
        count += ordinal and not (cardinal1 or cardinal2)
        cardinal1 = cardinal2
    
    return count
    

def count_edges(positions:Set[Position]) -> int:
    #Though the task asks for the number of edges, I'm really counting the number of corners which is the same.
    return sum([num_corners(pos, positions) for pos in positions])

def map_regions(data:np.ndarray) -> Dict[int, Set[Position]]:
    plant_regions = {}
    mapping = {}
    region = 0
    for plant in np.unique(data):
        mask = (data == plant)
        plant_positions = set(zip(*np.where(mask)))
        queue = {plant_positions.pop()}
        while True:
            #Explore region
            mapping[region] = set()
            while any(queue):
                (i, j) = queue.pop()
                queue.update({position for position in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if position in plant_positions})
                mapping[region].add((i, j))
                plant_positions -= {(i, j)}
            plant_positions -= mapping[region]
            region += 1

            #If all plots for given plant have been mapped, continue to the next plant, else initiate a new region.
            if any(plant_positions):
                queue = {plant_positions.pop()}
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
    areas = {region:len(region_mapping[region]) for region in region_mapping}
    perimeters = {region: 0 for region in region_mapping}
    for region in perimeters:
        for (i, j) in region_mapping[region]:
            perimeters[region] += not (i-1, j) in region_mapping[region]
            perimeters[region] += not (i+1, j) in region_mapping[region]
            perimeters[region] += not (i, j-1) in region_mapping[region]
            perimeters[region] += not (i, j+1) in region_mapping[region]
    
    fencing_price = sum([perimeters[region]*areas[region] for region in region_mapping])
    
    end = time.time()
    
    print("Total price of fencing:", fencing_price)
    print("Runtime for task 1:", end-start)

    #Task 2
    start = time.time()
    fencing_price = sum([count_edges(region_mapping[region])*areas[region] for region in region_mapping])
    end = time.time()
    print("Total price of fencing w/ bulk discount:", fencing_price)
    print("Runtime for task 2:", end-start)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())