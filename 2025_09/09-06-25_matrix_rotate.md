

# Matrix Rotate

## Prompt



Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. 

    
```
    rotate([[1, 2, 3], 				    [[7, 4, 1],
			[4, 5, 6],   should return   [8, 5, 2],
			[7, 8, 9]])  				 [9, 6, 3]]
```


## My Thoughts
This at first looked challenging until you notice the pattern. Lets call the rows `top_r and bottom_r`. After rotating the matrix. The bottom_r becomes the 1st column, and top_r becomes the 2nd column. All we had to do was create the columns calling ` zip(*matrix)` from that put it in the order from bottom row to top row by reversing it.

Given:
```Given:
[[1,2] if we   -->   [[3,1]
[3,4]] rotate  -->   [4,2]]
```


## Solution (Python)
```python
from typing import List

def rotate(matrix: List[List[int]]) -> List[List[int]]:

	return  [list(reversed(col))  for col in  zip(*matrix)]
```
