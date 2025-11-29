


# Ball Trajectory
## Prompt


Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (`2`), and the previous location of the ball (`1`), return the matrix indices for the next location of the ball.

-   The ball always moves in a straight line.
-   The movement direction is determined by how the ball moved from  `1`  to  `2`.
-   The edges of the matrix are considered walls. If the balls hits a:
    -   top or bottom wall, it bounces by reversing its vertical direction.
    -   left or right wall, it bounces by reversing its horizontal direction.
    -   corner, it bounces by reversing both directions.
## My Thoughts
The goal is to the find the coordinates of `1` which is the previous position and `2` which is the current position. We compute the movement vector `dr, dc` from `1` and `2`. The next move is `next = (r2  dr, c2 + dc)`. If that goes out the grid we know its a vertical or horizontal bounce. Then just return the new row or column.

## Solution (Python)
```python
def get_next_location(grid):
	rows = len(grid)
	cols = len(grid[0])

	prev_pos = None  # position of 1
	cur_pos = None  # position of 2

	for r in  range(rows):
		for c in  range(cols):
			if grid[r][c] == 1:
				prev_pos = (r, c)
			elif grid[r][c] == 2:
				cur_pos = (r, c)
				
	r1, c1 = prev_pos
	r2, c2 = cur_pos

	dr = r2 - r1
	dc = c2 - c1

	nr = r2 + dr
	nc = c2 + dc

	if nr < 0  or nr >= rows:
		dr = -dr
		nr = r2 + dr

	if nc < 0  or nc >= cols:
		dc = -dc
		nc = c2 + dc

	return  [nr, nc]
```
