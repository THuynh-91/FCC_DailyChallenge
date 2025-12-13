


# Game Of Life
## Prompt

Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

-   Each cell is either  `1`  (alive) or  `0`  (dead).
-   A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
-   Cells on the edges have fewer than eight neighbors.

Rules for updating each cell:

-   Any live cell with fewer than two live neighbors dies (underpopulation).
-   Any live cell with two or three live neighbors lives on.
-   Any live cell with more than three live neighbors dies (overpopulation).
-   Any dead cell with exactly three live neighbors becomes alive (reproduction).

For example, given:

```json
[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]

```

return:

```json
[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]

```

Each cell updates according to the number of live neighbors. For instance,  `[0][0]`  stays dead (2 live neighbors),  `[0][1]`  stays alive (2 live neighbors),  `[0][2]`  dies (3 live neighbors), and so on.

## My Thoughts
This was a pretty challenging problem. For each cell we have `(row, column) == (r, c)`. We then count live neighbors in the 8 surrounding positions... but we skip out of bounds.  
\
From that you apply the rules:
1. Live cell: survives if neighbors in `{2,3}` else dies
2. dead cell: becomes live if neighbors == `3`

## Solution (Python)
```python
def game_of_life(grid):
	rows = len(grid)
	cols = len(grid[0])  if rows > 0  else  0

	directions = [
		(-1,  -1), (-1,  0), (-1,  1),
		(  0,  -1), (  0,  1),
		(  1,  -1), (  1,  0), (  1,  1)

	]

	def live_neighbors(r, c):
		count = 0
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			if  0 <= nr < rows and  0 <= nc < cols:
				count += grid[nr][nc]
		return count

	next_grid = []
	for r in  range(rows):
		next_row = []
		for c in  range(cols):
			neighbors = live_neighbors(r, c)
			if grid[r][c] == 1:
				next_row.append(1  if neighbors in  (2,  3)  else  0)
			else:
				next_row.append(1  if neighbors == 3  else  0)
		next_grid.append(next_row)

	return next_grid

```
