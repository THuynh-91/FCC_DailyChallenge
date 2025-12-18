


# Checkerboard
## Prompt

Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with  `"X"`  and  `"O"`  characters of the given size.

-   The characters should alternate like a checkerboard.
-   The top-left cell must always be  `"X"`.

For example, given  `[3, 3]`, return:

```json
[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]
```

## My Thoughts
First I created an empty board `[]`. I looped over the rows and then for each row, create an empty list. I then loop over columns. Decide `X or O` using `(row + col) % 2`. We then append the row to the board and return the board.

## Solution (Python)
```python
def create_board(size):
	rows, cols = size
	board = []

	for r in  range(rows):
		row = []
		for c in  range(cols):
			if  (r + c) % 2 == 0:
				row.append("X")
			else:
				row.append("O")
		board.append(row)
	return board
```
