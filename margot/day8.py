import sys
import numpy as np

def main():
    path = "inputs/day8/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])

    antennas = {freq: {(i, j) for (i, j) in zip(*np.where(data == freq))} for freq in np.unique(data) if freq != '.'}
    
    #Task 1 
    antinodes = {}
    for freq in antennas:
        antinodes[freq] = set()
        for pos1 in antennas[freq]:
            i1, j1 = pos1
            antinodes[freq].update({(2*i1-i2, 2*j1-j2) for (i2, j2) in antennas[freq]-{pos1}})
        antinodes[freq] = {(i, j) for (i, j) in antinodes[freq] if (i >= 0 and j >= 0) and (i < data.shape[0] and j < data.shape[1])}
    all_antinodes = set().union(*antinodes.values())
    
    print("Number of unique antinode locations:", len(all_antinodes))
    
    
    return
    
if __name__ == "__main__":
    sys.exit(main())