import sys
import numpy as np
from typing import Dict, Set, Tuple

Frequency = str
Position = Tuple[int, int]
WaveVector = Tuple[int, int]

def in_grid(position:Position, data:np.ndarray) -> bool:
    x, y = position
    return (x >= 0 and y >= 0) and (x < data.shape[0] and y < data.shape[1])

def join_antinodes(antinodes:Dict[Frequency, Set[Position]]) -> Set[Position]:
    return set().union(*antinodes.values())
    
def main():
    path = "inputs/day8/"
    name = "input"
    
    with open(path+name+".txt") as file:
        data = np.array([list(line.strip()) for line in file])

    #Going to use Cartesian coordinates here, more intuitive when thinking about waves.
    antennas = {freq: {(x, y) for (x, y) in zip(*np.where(data == freq))} for freq in np.unique(data) if freq != '.'}
    
    #Even as a physicist I find this frequency talk confusing...
    #I think that antinodes are at multiples of the wave vector, i.e. the distance between antennas? 
    wavevectors = {freq:{(x1, y1):{(x1-x2, y1-y2) for (x2, y2) in antennas[freq]-{(x1, y1)}} for (x1, y1) in antennas[freq]} for freq in antennas}
    
    #(Task 1) Only consider antinodes which are one wave vector away.
    #I think the appropriate notation is lambda, so I will stick w/ this.
    antinodes = {freq:{(x+lamb_x, y+lamb_y) for (x, y) in antennas[freq] for (lamb_x, lamb_y) in wavevectors[freq][(x, y)] if in_grid((x+lamb_x, y+lamb_y), data)}
                           for freq in antennas}
    print("Number of unique antinode locations:", len(join_antinodes(antinodes)))
    
    #(Task 2) Consider all integer multiples. Could put some of this in a function but I think that'd just make it more confusing.
    antinodes = {freq:set() for freq in antennas}
    for freq in antennas:
        for pos in wavevectors[freq]:
            for (lamb_x, lamb_y) in wavevectors[freq][pos]:
                x, y = pos
                while in_grid((x, y), data):
                    antinodes[freq].add((x, y))
                    x += lamb_x
                    y += lamb_y
    print("Number of unique antinode locations for all integer multiples:", len(join_antinodes(antinodes)))
    
    return
    
if __name__ == "__main__":
    sys.exit(main())