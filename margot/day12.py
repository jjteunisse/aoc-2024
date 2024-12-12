import sys
import numpy as np
        

def main():
    path = "inputs/day12/"
    name = "test2"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])
        
    #Task 1
    areas = {plant:count for (plant, count) in zip(*np.unique(data, return_counts=True))}
    print("Areas:", areas)
    perimeters = {plant: 0 for plant in areas}
    for plant in perimeters:
        mask = (data == plant)
        for (i, j) in zip(*np.where(mask)):
            perimeters[plant] += (not mask[i-1, j] if i > 0 else 1)
            perimeters[plant] += (not mask[i+1, j] if i < mask.shape[0]-1 else 1)
            perimeters[plant] += (not mask[i, j-1] if j > 0 else 1)
            perimeters[plant] += (not mask[i, j+1] if j < mask.shape[1]-1 else 1)
    print("Perimeters:", perimeters)
    
    fencing_price = sum({perimeters[plant]*areas[plant] for plant in areas})
    print("Total price of fencing:", fencing_price)
    
    return
    
if __name__ == "__main__":
    sys.exit(main())