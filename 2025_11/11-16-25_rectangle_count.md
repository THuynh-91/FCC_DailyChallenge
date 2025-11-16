


# Rectangle Count

## Prompt


Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

-   Only count rectangles with integer width and height.

For example, given  `1`  and  `3`, return  `6`. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.

## My Thoughts
Essentially there is a formula for this. You choose a vertical and horizontal boundary then multiply them.

## Solution (Python)
```python
def count_rectangles(w, h):
	return  (w * (w + 1) // 2) * (h * (h + 1) // 2)
```
