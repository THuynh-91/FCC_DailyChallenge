



# Par for the Hole
## Prompt
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

-   `"Hole in one!"`  if it took one stroke.
-   `"Eagle"`  if it took two strokes less than par.
-   `"Birdie"`  if it took one stroke less than par.
-   `"Par"`  if it took the same number of strokes as par.
-   `"Bogey"`  if it took one stroke more than par.
-   `"Double bogey"`  if took two strokes more than par

## My Thoughts
I could have done a map, but this was simpler. We check for each cases regarding the par and strokes.

## Solution (Python)
```python
def golf_score(par, strokes):
	if strokes == 1:
		return  "Hole in one!"
	elif strokes == par - 2:
		return  "Eagle"
	elif strokes == par - 1:
		return  "Birdie"
	elif strokes == par:
		return  "Par"
	elif strokes == par + 1:
		return  "Bogey"
	elif strokes == par + 2:
		return  "Double bogey"
```
