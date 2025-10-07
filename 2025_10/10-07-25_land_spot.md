

#  Landing Spot
## Prompt

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

-   Each spot in the matrix will contain a number from  `0-9`, inclusive.
-   Any  `0`  represents a potential landing spot.
-   Any number other than  `0`  is too dangerous to land. The higher the number, the more dangerous.
-   The safest spot is defined as the  `0`  cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
-   Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
-   Return the indices of the safest landing spot. There will always only be one safest spot.

## My Thoughts
My though process through this was just to find the 0s, and then add up the numbers in the adjacent and return the position with the smallest sum of adjacency.

## Solution (Python)
```python
def find_landing_spot(grid):
	rows = len(grid)
	cols = len(grid[0])
	best_pos = [-1,  -1]
	best_sum = 10**9


	for r in  range(rows):
		for c in  range(cols):
			if grid[r][c] != 0:
				continue
				
		danger = 0
		if r > 0: danger += grid[r - 1][c]
		if r < rows - 1: danger += grid[r + 1][c]
		if c > 0: danger += grid[r][c - 1]
		if c < cols - 1: danger += grid[r][c + 1]

	if danger < best_sum:
		best_sum = danger
		best_pos = [r, c]
		
	return best_pos
```

