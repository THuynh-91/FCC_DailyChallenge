

#  Weekday Finder
## Prompt

Given a string date in the format  `YYYY-MM-DD`, return the day of the week.

Valid return days are:

-   `"Sunday"`
-   `"Monday"`
-   `"Tuesday"`
-   `"Wednesday"`
-   `"Thursday"`
-   `"Friday"`
-   `"Saturday"`

Be sure to ignore time zones.

## My Thoughts
Really simple problem. Use the datetime library.

## Solution (Python)
```python
from datetime import datetime

def get_weekday(date_string):
	date_obj = datetime.strptime(date_string,  "%Y-%m-%d")
	day = date_obj.strftime("%A")

	return day
```

