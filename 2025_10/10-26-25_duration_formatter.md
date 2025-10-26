

#  Duration Formatter
## Prompt
Given an integer number of seconds, return a string representing the same duration in the format  `"H:MM:SS"`, where  `"H"`  is the number of hours,  `"MM"`  is the number of minutes, and  `"SS"`  is the number of seconds. Return the time using the following rules:

-   Seconds: Should always be two digits.
-   Minutes: Should omit leading zeros when they aren't needed. Use  `"0"`  if the duration is less than one minute.
-   Hours: Should be included only if they're greater than zero.
For example, given  `"ACGT"`, return  `"TGCA"`.

## My Thoughts
I just formatted the requirements per say, it was a typical and easy assiggnment.

## Solution (Python)
```python
def  format(seconds):
	hh = seconds // 3600
	seconds %= 3600
	mm = seconds // 60
	ss = seconds % 60

	ss = f"{ss:02d}"
	
	if hh > 0:
		return f"{hh}:{mm:02d}:{ss}"
	else:
		return f"{mm}:{ss}"
```

