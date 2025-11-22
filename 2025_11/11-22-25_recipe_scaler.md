


# Recipe Scaler
## Prompt

Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

-   Each item in the given array will be a string in the format:  `"quantity unit ingredient"`. For example  `"2 C Flour"`.
-   Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
-   Return the scaled items in the same order they are given.

## My Thoughts
Essentially the array is split into quantity, unit, and ingredient. I just had to extract all those parts and multiply the quantity by the scale and join them all back together.

## Solution (Python)
```python
def smart_number(value):
	f = float(value)
	return  int(f)  if f.is_integer()  else f

  

def scale_recipe(ingredients, scale):
	res = []

	for i in ingredients:
		parts = i.split()
		item1 = parts[0]
		item2 = parts[1]
		item3 = " ".join(parts[2:])
		new = float(item1) * scale
		item1 = smart_number(new)
		update = f"{item1} {item2} {item3}"
		res.append(update)
	return res
```
