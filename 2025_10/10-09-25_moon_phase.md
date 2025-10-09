

#  Moon Phase
## Prompt



For day six of Space Week, you will be given a date in the format  `"YYYY-MM-DD"`  and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

-   `"New"`: days 1 - 7
-   `"Waxing"`: days 8 - 14
-   `"Full"`: days 15 - 21
-   `"Waning"`: days 22 - 28

After day 28, the cycle repeats with day 1, a new moon.

-   Use  `"2000-01-06"`  as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
-   You will not be given any dates before the reference date.
-   Return the correct phase as a string.

## My Thoughts
The initial idea was just to create a set of the days in a month, subtract that from the reference, however that sounded a bit too tedious. Therefore I just used the datetime import to simplify most of the steps. Then just grabbed the moon phase.

## Solution (Python)
```python
from datetime import datetime

def moon_phase(date_str):
	reference = datetime.strptime("2000-01-06",  "%Y-%m-%d")
	given_date = datetime.strptime(date_str,  "%Y-%m-%d")
	days_diff = (given_date - reference).days
	cycle_day = (days_diff % 28) + 1
	
	if  1 <= cycle_day <= 7:
		return  "New"
	elif  8 <= cycle_day <= 14:
		return  "Waxing"
	elif  15 <= cycle_day <= 21:
		return  "Full"
	else:
		return  "Waning"
```

