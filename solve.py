'''
Return number of cells that fall within N steps of any positive values in a 2d array
Step distance is defined by Manhattan Distance: abs(y1-y2) + abs(x1-x2)
Array does not wrap unless height and/or width is less than 3

Reqs
[x] Each cell in neighborhood should be counted *only once* regardless of how many neighborhoods its in
[x] Cell containing positive value should also count as a member

Assumptions
[ ] 2d array, positive number in each
[ ] width and height greater than 0
[ ] (Y, X) notation, like numpy
[ ] Manhattan distance: abs(y1-y2) + abs(x1-x2)
[ ] Initially, dimensions dont wrap around the grid

Expansion question possibilities
"what if it does wrap for all sizes"

Optimizations
short circuit if candidate cell falls within a certain range based on WxH
'''

import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
import numpy as np

def visualize_hood(grid_x, grid_y, candidates):
  coords = [sublist for lists in candidates.values() for sublist in lists]
  print(coords)

  # Build a tight grid
  xmin, xmax = 0, grid_x
  ymin, ymax = 0, grid_y

  # matrix syntax, y, x
  grid = np.zeros((grid_y, grid_x))

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
        # no wraparound
        if (x < 0) or (y < 0):
          continue
        cells.append( (x, y) )
  print(f'Candidates size: {len(cells)}')
  return cells

def num_cells(arr, steps: int):
  print(f'steps: {steps}')
  # find all positive values in the array
  candidates = np.argwhere(arr > 0)

  # for each candidate, find valid cells within steps distance
  # data structure example, key must be hashable, value is list of tuples for later dedup as set
  # {(np.int64(3), np.int64(3)): [], (np.int64(7), np.int64(7)): []}
  candidates = {tuple(candidates): [] for candidates in candidates}
  print(f'candidates: {candidates}')

  # Find the neighborhood. calc manhattan distance from cell
  for c in candidates:
    candidates[c] = manhattan_distance(c, steps)
  print(candidates)

  # visual sanity check of 2d array
  # matrix notation for numpy, arr.shape is tuple (y,x)
  visualize_hood(arr.shape[1], arr.shape[0], candidates)

  # get list of all coordinates, convert list 
  # coords = [sublist for lists in candidates.values() for sublist in lists]
  coords = []
  for cells in candidates.values():
    for cell in cells:
      coords.append(cell)
  print(f'All coords before unique filtering for overlap: {coords}')
  return len(set(coords))

  # remove/redundant bc now using tuples from start (filter duplicates, retaining one copy)
  #unique = [list(t) for t in {tuple(x) for x in coords}]
  #return len(unique)

if __name__ == '__main__':
  # (y, x) notation
  # use pytest

  # one positive cell fully contained on grid
  # return 25
  ex_1 = np.zeros((11,11))
  ex_1[5,5] = 9
  print(f'\033[92m Neighbors: {num_cells(ex_1, 3)} == 25 \033[0m')

  # one positive cell near edge
  # return 21
  ex_2 = np.zeros((11,11))
  ex_2[1,5] = 9
  print(f'\033[92m Neighbors: {num_cells(ex_2, 3)} == 21 \033[0m')

  # two positive values with disjoint neighborhoods
  # return 26
  ex_3 = np.zeros((11,11))
  ex_3[3,3] = 9
  ex_3[7,7] = 9
  print(f'\033[92m Neighbors: {num_cells(ex_3, 2)} == 26 \033[0m')

  # two positive values with overlapping neighborhoods
  # test counting of candidate cells only once per grid
  # return 22
  # 23 should be the correct answer?
  # the overlap is 3 cells
  ex_4 = np.zeros((11,11))
  ex_4[3,3] = 9
  ex_4[5,5] = 9
  print(f'\033[92m Neighbors: {num_cells(ex_4, 2)} == 22 \033[0m')

  # two positive values with one running off
  # should have 1 cell clipped
  # return 22
  ex_5 = np.zeros((11,11))
  ex_5[3,3] = 9
  ex_5[1,5] = 9
  print(f'\033[92m Neighbors: {num_cells(ex_5, 2)} == 22 \033[0m')

  # oddly shaped array, long x axis
  ex_6 = np.zeros((15, 30))
  ex_6[3,3] = 9
  ex_6[7,7] = 9
  print(f'\033[92m Neighbors: {num_cells(ex_6, 2)} == 26 \033[0m')







