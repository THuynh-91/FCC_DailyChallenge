


# Miles to Kilometers
## Prompt

Given a distance in miles as a number, return the equivalent distance in kilometers.

-   The input will always be a non-negative number.
-   1 mile equals 1.60934 kilometers.
-   Round the result to two decimal places.
    

If the given sentence meets any of the rules above, return  `"AI"`, otherwise, return  `"Human"`.
## My Thoughts
Multiply the conversion rates then round it.

## Solution (Python)
```python
def convert_to_km(miles):
	return  round(miles * 1.60934,  2)
```
