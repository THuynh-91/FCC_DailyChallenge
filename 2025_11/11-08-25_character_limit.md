

#  Character Limit
## Prompt

In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

-   `"short post"`  if it fits within a 40-character limit.
-   `"long post"`  if it's greater than 40 characters and fits within an 80-character limit.
-   `"invalid post"`  if it's too long to fit within either limit.

## My Thoughts
Not much thinking behind it, complete the restrictions.

## Solution (Python)
```python
def can_post(message):
	length = len(message)
	if length < 40:
		return  "short post"
	if length < 80:
		return  "long post"
	return  "invalid post"
```

