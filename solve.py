'''
Return number of cells that fall within N steps of any positive values in a 2d array
Step distance is defined by Manhattan Distance: abs(x1-x2) + abs(y1-y2)
Array does not wrap unless height and/or width is less than 3

Expansion question possibilities
"what if it does wrap for all sizes"

Optimizations
short circuit if candidate cell falls within a certain range based on WxH
'''

import matplotlib.pyplot as plt
import numpy as np

def visualize_hood(grid_x, grid_y, coords):

  coords = np.array(coords)
  x, y = coords[:, 0], coords[:, 1]

  # Build a tight grid
  xmin, xmax = 0, grid_x
  ymin, ymax = 0, grid_y

  grid = np.zeros((grid_x, grid_y))

  for xi, yi in coords:
    grid[yi - ymin, xi - xmin] = 1  # note: [y, x]

  fig, ax = plt.subplots(figsize=(grid_x, grid_y))

  ax.imshow(grid, origin='lower')

  # Grid lines (clean, square cells)
  ax.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
  ax.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
  ax.grid(which="minor")

  # Tick labels as real coordinates
  ax.set_xticks(np.arange(grid.shape[1]))
  ax.set_yticks(np.arange(grid.shape[0]))
  ax.set_xticklabels(np.arange(0, grid_x))
  ax.set_yticklabels(np.arange(0, grid_y))

  ax.set_aspect('equal')

  # Clean framing
  ax.set_title("Manhattan Neighborhood", pad=12)
  ax.set_xlabel("X")
  ax.set_ylabel("Y")

  plt.tight_layout()
  plt.show()

def manhattan_distance(c, n):
  cells = []
  c_x, c_y = c[0], c[1]
  for x in range(c_x - n, c_x + n+1):
    for y in range(c_y - n, c_y + n+1):
      man_dist = abs(x - c_x) + abs(y - c_y)
      if man_dist <= n:
        print(f'[+] {man_dist}')
        cells.append( [x, y] )
  print(f'Candidates size: {len(cells)}')
  return cells

def num_cells(arr, steps: int):
  print(f'steps: {steps}')
  # find all positive values in the array
  candidates = np.argwhere(arr > 0)

  # for each candidate, find valid cells within steps distance
  candidates = {tuple(candidates): [] for candidates in candidates}
  print(f'candidates: {candidates}')

  # Find the neighborhood. calc manhattan distance from cell
  for c in candidates:
    candidates[c] = manhattan_distance(c, steps)
  print(candidates)

  visualize_hood(11, 11, candidates[(5,5)])

  # mask invalid results (wrapping) based on NxM condition

if __name__ == '__main__':
  test = np.zeros((11,11))
  test[5, 5] = 5
  print(test)
  num_cells(test, 3)
