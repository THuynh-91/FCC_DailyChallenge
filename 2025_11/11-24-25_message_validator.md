


# Message Validator
## Prompt

Given a message string and a validation string, determine if the message is valid.

-   A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
-   Letters are case-insensitive.
-   Words in the message are separated by single spaces.

## My Thoughts
Go through the text and split and grab the first character and then combine it and then compare it to the validation.

## Solution (Python)
```python
def is_valid_message(message, validation):
	msg = message.split()
	res = ''

	for i in msg:
		res += i[0]
	return res.lower() == validation.lower()
```
