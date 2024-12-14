import sys
import re
from typing import Tuple, List, Iterator
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

Position = Tuple[int, int]
Velocity = Tuple[int, int]
Frame = np.ndarray

class RobotSimulation():
    #This is a bit like a molecular dynamics simulation isn't it? 
    def __init__(self, width:int, height:int, positions:List[Position], velocities:List[Velocity]) -> None:
        self.width = width
        self.height = height
        self.positions = np.array(positions)
        self.velocities = np.array(velocities)
        
    def update(self, seconds:int) -> None:
        self.positions[:, 0] = (self.positions[:, 0] + seconds*self.velocities[:, 0])%self.height
        self.positions[:, 1] = (self.positions[:, 1] + seconds*self.velocities[:, 1])%self.width
        
    def run(self, num_frames:int, update_interval=1) -> Iterator[Frame]:
        frame = np.zeros((self.height, self.width), dtype=bool)
        for i in range(num_frames):
            frame[:, :] = False
            frame[self.positions[:, 0], self.positions[:, 1]] = True
            yield frame
            
            self.update(update_interval)
        
def animate(framedat:Tuple[int, Frame]):
    i, frame = framedat
    
    ax = plt.gca()
    
    ax.clear()
    image = np.ones((*frame.shape, 3))
    image[frame] = [0, 1, 0]
    ax.imshow(image)
    
    plt.title("Iteration {}".format(i))
    
    return ax
    
        
def safety_factor(robsim:RobotSimulation) -> int:
    first = sum([(i < robsim.height//2 and j < robsim.width//2) for (i, j) in robsim.positions])
    second = sum([(i < robsim.height//2 and j > robsim.width//2) for (i, j) in robsim.positions])
    third = sum([(i > robsim.height//2 and j < robsim.width//2) for (i, j) in robsim.positions])
    fourth = sum([(i > robsim.height//2 and j > robsim.width//2) for (i, j) in robsim.positions])
    
    return first*second*third*fourth

def main():
    path = "inputs/day14/"
    name = "input"
    
    pattern = re.compile("p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)")
    positions = []
    velocities = []
    with open(path+name+".txt") as file:
        for line in file:
            groups = pattern.match(line).groups()
            positions.append((int(groups[1]), int(groups[0])))
            velocities.append((int(groups[3]), int(groups[2])))
            
    width = 101
    height = 103
    seconds = 100
            
    #Task 1
    robsim = RobotSimulation(width, height, positions, velocities)
    robsim.update(seconds)
    
    print("Safety factor:", safety_factor(robsim))
    
    #(Task 2) ...what? Guess it's animating time.
    robsim = RobotSimulation(width, height, positions, velocities)
    fig = plt.figure()
    
    #I see a promising structure appearing starting at iteration 14, and repeating every 101 frames. Try to look at these frames alone.
    robsim.update(14)
    ani = FuncAnimation(fig, animate, enumerate(robsim.run(73, 101)), interval=1, cache_frame_data=False, repeat=False)
    
    plt.show()
    
    #I find that the Christmas tree appears after 72 iterations of size 101 with starting number 14, which gives 7286.
    
    return
    
if __name__ == "__main__":
    sys.exit(main())