import sys
import numpy as np
from typing import Tuple, Dict, Set
        
Position = Tuple[int, int]
        
def map_regions(data:np.ndarray) -> Dict[int, Set[Position]]:
    plant_regions = {}
    mapping = {}
    for plant in np.unique(data):
        mask = (data == plant)
        plant_iterator = zip(*np.where(mask))
        plant_regions[plant] = [len(mapping)+1]
        mapping[len(mapping)+1] = {next(plant_iterator)}
        for (i, j) in plant_iterator:
            connected = False
            for region in plant_regions[plant]:
                if ((i-1, j) in mapping[region]) or ((i, j-1) in mapping[region]):
                    mapping[region].add((i, j))
                    connected = True
                    break
            if not connected:
                plant_regions[plant].append(len(mapping)+1)
                mapping[len(mapping)+1] = {(i, j)}
    print(plant_regions)
    return mapping

def main():
    path = "inputs/day12/"
    name = "test2"
    
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
    for region in region_mapping:
        print(region, areas[region], perimeters[region])
    
    
    fencing_price = sum({perimeters[region]*areas[region] for region in region_mapping})
    print("Total price of fencing:", fencing_price)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())