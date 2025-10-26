

#  Hidden Treasure
## Prompt

Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates (`[row, column]`) for the next dive of your treasure search, return  `"Empty"`,  `"Found"`, or  `"Recovered"`  using the following rules:

-   The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.
    
-   Each cell in the 2D array will contain one of the following values:
    
    -   `"-"`: No treasure.
    -   `"O"`: A part of the treasure that has not been found.
    -   `"X"`: A part of the treasure that has already been found.
-   If the dive location has no treasure, return  `"Empty"`.
    
-   If the dive location finds treasure, but at least one other part of the treasure remains unfound, return  `"Found"`.
    
-   If the dive location finds the last unfound part of the treasure, return  `"Recovered"`.

## My Thoughts
Just finding the mark through the array with the row column as coordinates.

## Solution (Python)
```python
def dive(grid, coord):
	r, c = coord
	cell = grid[r][c]
	if cell == "-":
		return  "Empty"
	remaining_O = sum(row.count("O")  for row in grid)
	if cell == "O"  and remaining_O == 1:
		return  "Recovered"
	return  "Found"

```

