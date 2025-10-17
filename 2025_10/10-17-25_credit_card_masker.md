#  Credit Card Masker
## Prompt
Given a string of credit card numbers, return a masked version of it using the following constraints:

-   The string will contain four sets of four digits (`0-9`), with all sets being separated by a single space, or a single hyphen (`-`).
-   Replace all numbers, except the last four, with an asterisk (`*`).
-   Leave the remaining characters unchanged.

For example, given  `"4012-8888-8888-1881"`  return  `"****-****-****-1881"`.

## My Thoughts
This was pretty simple. I went through the digits until the last 4 digits of the card. If the character was a digit I basically censored it or replaced it with a star. Then I concatenated it with the last 4 digits of the original card.

## Solution (Python)
```python
def mask(card):
	digits = "0123456789"
	res = ""

	for ch in card[:-4]:
		if ch in digits:
			res += "*"
		else:
			res += ch
	res += card[-4:]

	return res
```

