import sys
import numpy as np
from typing import Tuple, Dict, Set, List
        
Position = Tuple[int, int]

def neighbours(position:Position) -> List[Position]:
    i, j = position
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        
def map_regions(data:np.ndarray) -> Dict[int, Set[Position]]:
    plant_regions = {}
    mapping = {}
    region = 0
    for plant in np.unique(data):
        mask = (data == plant)
        plant_positions = set(zip(*np.where(mask)))
        queue = [plant_positions.pop()]
        while True:
            mapping[region] = set()
            while any(queue):
                queue.extend([position for position in neighbours(queue[0]) if position in plant_positions-mapping[region]])
                mapping[region].add(queue.pop(0))
            plant_positions -= mapping[region]
            region += 1
            if any(plant_positions):
                queue = [plant_positions.pop()]
            else:
                break
        
    return mapping

def main():
    path = "inputs/day12/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    region_mapping = map_regions(data)
    
    #Task 1
    areas = {region:len(region_mapping[region]) for region in region_mapping}
    perimeters = {region: 0 for region in region_mapping}
    for region in perimeters:
        for (i, j) in region_mapping[region]:
            perimeters[region] += not (i-1, j) in region_mapping[region]
            perimeters[region] += not (i+1, j) in region_mapping[region]
            perimeters[region] += not (i, j-1) in region_mapping[region]
            perimeters[region] += not (i, j+1) in region_mapping[region]
    
    
    fencing_price = sum({perimeters[region]*areas[region] for region in region_mapping})
    print("Total price of fencing:", fencing_price)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())