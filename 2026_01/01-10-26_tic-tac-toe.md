
# Tic-Tac-Toe
## Prompt

Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

-   Each element in the given matrix is either an  `"X"`  or  `"O"`.

A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

-   `"X wins"`  if player X has three in a row.
-   `"O wins"`  if player O has three in a row.
-   `"Draw"`  if no player has three in a row.

## My Thoughts
The key idea is to collect all possible lines. We check if any line is all `"X"` or `"O"`. We return the result accordingly.

## Solution (Python)
```python
def tic_tac_toe(board):
	lines = []
	lines.extend(board)

	for col in  range(3):
		lines.append([board[row][col]  for row in  range(3)])

	lines.append([board[i][i]  for i in  range(3)])
	lines.append([board[i][2 - i]  for i in  range(3)])

	for line in lines:
		if line == ["X",  "X",  "X"]:
			return  "X wins"
		if line == ["O",  "O",  "O"]:
			return  "O wins"

	return  "Draw"
```
