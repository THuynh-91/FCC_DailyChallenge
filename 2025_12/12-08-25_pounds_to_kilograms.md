


#  Pounds to Kilograms
## Prompt


Given a weight in pounds as a number, return the string  `"(lbs) pounds equals (kgs) kilograms."`.

-   Replace  `"(lbs)"`  with the input number.
-   Replace  `"(kgs)"`  with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
-   1 pound equals 0.453592 kilograms.
-   If the input is  `1`, use  `"pound"`  instead of  `"pounds"`.
-   If the converted value is  `1`, use  `"kilogram"`  instead of  `"kilograms"`.

For example, given  `"yes yes yes please"`, return  `"yes(3) please"`.
## My Thoughts
It was just converting, the main thing was just formatting and getting it right for the niche situations. 

## Solution (Python)
```python
def convert_to_kgs(lbs):
	kgs = round(lbs * 0.453592,  2)

	pound = 'pound'  if lbs == 1  else  'pounds'
	kilogram = 'kilogram'  if kgs == 1  else  'kilograms'

	return f'{lbs} {pound} equals {kgs:.2f} {kilogram}.'

```
