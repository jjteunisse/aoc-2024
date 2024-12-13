import sys
import numpy as np
from typing import Tuple, Dict, Set
import time
        
Position = Tuple[int, int]

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
    name = "input"
    
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
    
    return
    
if __name__ == "__main__":
    sys.exit(main())