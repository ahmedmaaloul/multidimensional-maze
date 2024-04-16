from path_finder import PathFinder3D
import numpy as np

# Initialize the path finder
my_path_finder = PathFinder3D()

np.random.seed(41)

# Example of a 3D map
maze_3d = np.random.randint(low=0, high=2, size=(3,3,3))

# Find path from start to stop
start = [0,0,0]
stop = [2,2,1]
path = my_path_finder.find_path(maze_3d, start, stop)

# Output the path
print("Path:", path)
