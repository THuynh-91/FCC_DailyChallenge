

# Is It The Weekend?
## Prompt


Given a date in the format  `"YYYY-MM-DD"`, return the number of days left until the weekend.

-   The weekend starts on Saturday.
-   If the given date is Saturday or Sunday, return  `"It's the weekend!"`.
-   Otherwise, return  `"X days until the weekend."`, where  `X`  is the number of days until Saturday.
-   If  `X`  is  `1`, use  `"day"`  (singular) instead of  `"days"`  (plural).
-   Make sure the calculation ignores your local timezone.

## My Thoughts
Essentially parse the string and grab the weekday then check the difference from the upcoming Saturday.

## Solution (Python)
```python
from datetime import datetime

def days_until_weekend(date_str):
	d = datetime.strptime(date_str,  "%Y-%m-%d")
	wd = d.weekday()
	if wd >= 5:
		return  "It's the weekend!"
	days_left = 5 - wd
	unit = "day"  if days_left == 1  else  "days"

	return f"{days_left} {unit} until the weekend."
```

