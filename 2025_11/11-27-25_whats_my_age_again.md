


# Whats My Age Again
## Prompt
Given the date of someone's birthday in the format  `YYYY-MM-DD`, return the person's age as of November 27th, 2025.

-   Assume all birthdays are valid dates before November 27th, 2025.
-   Return the age as an integer.
-   Be sure to account for whether the person has already had their birthday in 2025.

## My Thoughts
Convert the birthdate into year, month day, then compare it with the date. We grab the age and check if they had their birthday yet.

## Solution (Python)
```python
from datetime import date

 
def calculate_age(bday):
	birth_year, birth_month, birth_day = map(int, bday.split("-"))
	today = date(2025,  11,  27)
	age = today.year - birth_year

	if  (birth_month, birth_day) > (today.month, today.day):
		age -= 1

	return age
```
