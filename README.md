# PathFinder3D

PathFinder3D is a Python module for finding paths in a three-dimensional grid using Breadth-First Search (BFS). It is designed to navigate through a 3D space where each cell in the space can either be passable (represented by 0) or blocked (represented by 1).

## Installation

No external dependencies are required for this module, as it only uses `numpy` and Python's built-in libraries. Ensure you have Python and `numpy` installed:

```bash
pip install numpy
```

## Usage

1. Import the PathFinder3D class from the module.
2. Create an instance of PathFinder3D.
3. Define a 3D numpy array where cells are marked as 0 for passable and 1 for blocked.
4. Use the `find_path` method to find a path from a start coordinate to an end coordinate.

Example:

```python
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
```

## Features

- **3D Grid Navigation:** Navigate through any 3D grid of dimensions n x m x k.
- **Breadth-First Search:** Utilizes BFS to ensure the shortest path is found.
- **Path Tracking:** Tracks and returns the complete path from start to finish if available.


## License

This project is open-source and available under the MIT License.