import sys
import numpy as np
from typing import Dict, Set, Tuple

Frequency = str
Position = Tuple[int, int]

def all_antinodes(antinodes:Dict[Frequency, Set[Position]]) -> Set[Position]:
    return set().union(*antinodes.values())

def main():
    path = "inputs/day8/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])

    #Going to use Cartesian coordinates here, more intuitive when thinking about waves.
    antennas = {freq: {(x, y) for (x, y) in zip(*np.where(data == freq))} for freq in np.unique(data) if freq != '.'}
    
    #Task 1 
    antinodes = {}
    for freq in antennas:
        #Generate antinodes.
        antinodes[freq] = {(2*x1-x2, 2*y1-y2) for (x1, y1) in antennas[freq] for (x2, y2) in antennas[freq]-{(x1, y1)}}
        #Check that antinodes fall within input matrix. 
        antinodes[freq] = {(x, y) for (x, y) in antinodes[freq] if (x >= 0 and y >= 0) and (x < data.shape[0] and y < data.shape[1])}
    
    print("Number of unique antinode locations:", len(all_antinodes(antinodes)))
    
    #(Task 2) Even as a physicist I find this frequency talk confusing...
    #I think that antinodes are at multiples of the wave vector, i.e. the distance between antennas? 
    wavevectors = {freq:{(x1, y1):{(x1-x2, y1-y2) for (x2, y2) in antennas[freq]-{(x1, y1)}} for (x1, y1) in antennas[freq]} for freq in antennas}
    
    antinodes = {freq:set() for freq in antennas}
    for freq in antennas:
        #I think the typical notation is k for the wave vector, so I will stick w/ this.
        for pos in wavevectors[freq]:
            for (kx, ky) in wavevectors[freq][pos]:
                x, y = pos
                while (x >= 0 and y >= 0) and (x < data.shape[0] and y < data.shape[1]):
                    antinodes[freq].add((x, y))
                    x += kx
                    y += ky
    print("Number of unique antinode locations for all integer multiples:", len(all_antinodes(antinodes)))
    
    return
    
if __name__ == "__main__":
    sys.exit(main())