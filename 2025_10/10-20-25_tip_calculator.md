

#  Tip Calculator
## Prompt

Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

-   Prices will be given in the format:  `"$N.NN"`.
-   Custom tip percents will be given in this format:  `"25%"`.
-   Return amounts in the same  `"$N.NN"`  format, rounded to two decimal places.

For example, given a  `"$10.00"`  meal price, and a  `"25%"`  custom tip value, return  `["$1.50", "$2.00", "$2.50"]`.

## My Thoughts


Strip the **`$`** sign and convert meal price to a float.
Remove the **`%`** sign and convert the custom tip percent to a float.
 Compute:
15% tip → `price * 0.15`
20% tip → `price * 0.20`
custom tip → `price * (custom / 100)`
Format each tip to **`"$N.NN"`**, rounding to 2 decimals.

## Solution (Python)
```python
def calculate_tips(price:  str, custom:  str):
	meal = float(price.strip("$"))
	custom_percent = float(custom.strip("%"))
	tips = [
		meal * 0.15,
		meal * 0.20,
		meal * (custom_percent / 100)
	]
	return  [f"${tip:.2f}"  for tip in tips]
```

