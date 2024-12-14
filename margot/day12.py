import sys
import numpy as np
from typing import Tuple, Dict, Set
import time
        
Position = Tuple[int, int]

def num_corners(pos:Position, positions:Set[Position]):
    i, j = pos
    top = (i-1, j) in positions
    bottom = (i+1, j) in positions
    left = (i, j-1) in positions
    right = (i, j+1) in positions
    is_vertical_edge = top and bottom
    is_horizontal_edge = left and right

    if is_horizontal_edge or is_vertical_edge:
        return 0
    elif (top or bottom) and (left or right):
        return 1
    elif (top or bottom) or (left or right):
        return 2
    else:
        return 4

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

            if any(plant_positions):
                queue = {plant_positions.pop()}
            else:
                break
        
    return mapping

def main():
    path = "inputs/day12/"
    name = "test"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    
    #Task 1
    start = time.time()
    
    region_mapping = map_regions(data)
    
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
    print("Runtime:", end-start)

    #Task 2
    for region in areas:
        print(region, region_mapping[region], areas[region], count_edges(region_mapping[region]))

    fencing_price = sum([count_edges(region_mapping[region])*areas[region] for region in region_mapping])
    print("Total price of fencing w/ bulk discount:", fencing_price)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())