

#  Signature Validation
## Prompt

Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

-   Letters in the message and secret key have these values:
    -   `a`  to  `z`  have values  `1`  to  `26`  respectively.
    -   `A`  to  `Z`  have values  `27`  to  `52`  respectively.
-   All other characters have no value.
-   Compute the signature by taking the sum of the message plus the sum of the secret key.

For example, given the message  `"foo"`  and the secret key  `"bar"`, the signature would be  `57`:

```md
f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
```

## My Thoughts
This question was pretty fun. I imported the alphabet which had indexes of `0-51`. I was thinking to inserting an element to the very beginning to make them the correct index value, but that might have gone wrong if the temp was actually used in the sentence giving a value it wasn't supposed to. I ended up doing it the normal way and incrementing the value by 1.

## Solution (Python)
```python
import string

all_letters = string.ascii_letters

def verify(message, key, signature):
	ms = 0
	ky = 0
	for ch in message:
		if ch in all_letters:
			ms += all_letters.index(ch) + 1
	 
	for ch in key:
		if ch in all_letters:
			ky += all_letters.index(ch) + 1
	res = ms + ky
	
	return res == signature
```

