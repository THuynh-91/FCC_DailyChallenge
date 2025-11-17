

# Fingerprint Test
## Prompt
Given two strings representing fingerprints, determine if they are a match using the following rules:

-   Each fingerprint will consist only of lowercase letters (`a-z`).
-   Two fingerprints are considered a match if:
    -   They are the same length.
    -   The number of differing characters does not exceed 10% of the fingerprint length.

## My Thoughts
Pretty simple solution, weirdly enough I thought that the difference characters was somehow the difference in length of characters on the string index alphabet not just actual different characters, therefore it was a lot more complicated then I wanted it to be so I had to restructure it.

## Solution (Python)
```python
def is_match(fingerprint_a, fingerprint_b):=	
	if  len(fingerprint_a) != len(fingerprint_b):
		return  False

	diff = 0

	for i in  range(len(fingerprint_a)):
		temp = 0
		a = fingerprint_a[i]
		b = fingerprint_b[i]
		if a != b:
			diff += 1

	if diff > (len(fingerprint_a) * 0.1):
		return  False
	return  True
```

