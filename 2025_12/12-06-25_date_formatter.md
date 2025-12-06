


#  Date Formatter
## Prompt
Given a date in the format  `"Month day, year"`, return the date in the format  `"YYYY-MM-DD"`.

-   The given month will be the full English month name. For example:  `"January"`,  `"February"`, etc.
-   In the return value, pad the month and day with leading zeros if necessary to ensure two digits.

For example, given  `"December 6, 2025"`, return  `"2025-12-06"`.
## My Thoughts
I just had to map out the worded form to the number correspondent and then return the correct format.

## Solution (Python)
```python
def format_date(date_str):
	months = {
	"January":  "01",  "February":  "02",  "March":  "03",
	"April":  "04",  "May":  "05",  "June":  "06",
	"July":  "07",  "August":  "08",  "September":  "09",
	"October":  "10",  "November":  "11",  "December":  "12"
	}

	month_name, rest = date_str.split(" ",  1)
	day_str, year_str = rest.split(", ")

	month = months[month_name]
	day = day_str.zfill(2)
	return f"{year_str}-{month}-{day}"
```
