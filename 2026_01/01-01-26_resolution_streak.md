



# Resolution Streak
## Prompt

Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

-   The first sub-array is day 1, and second day 2, and so on.

A day is considered successful if all three of the following goals are met:

-   You walked at least 10,000 steps.
-   You had no more than 120 minutes of screen time.
-   You read at least five pages.

If all of the given days are successful, return  `"Resolution on track: N day streak."`  Where  `N`  is the number of successful days.

If one or more days is not a success, return  `"Resolution failed on day X: N day streak."`. Where  `X`  is the day number of the first unsuccessful day, and  `N`  is the number of successful days before the first unsuccessful day.

## My Thoughts
The key idea to do this is that each day is `[steps, screen_time, pages_read]`. We then count a successful day is all three are true from the prompt above. We just scan the days in order and count how many days in a row are successful.

## Solution (Python)
```python
def resolution_streak(days):
	streak = 0

	for i, day in  enumerate(days):
		steps, screen, pages = day
		if steps >= 10000  and screen <= 120  and pages >= 5:
			streak += 1
		else:
			return f"Resolution failed on day {i + 1}: {streak} day streak."

	return f"Resolution on track: {streak} day streak."
	```
