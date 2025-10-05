

#  P@ssw0rd Str3ngth!
## Prompt

Given a password string, return  `"weak"`,  `"medium"`, or  `"strong"`  based on the strength of the password.

A password is evaluated according to the following rules:

-   It is at least 8 characters long.
-   It contains both uppercase and lowercase letters.
-   It contains at least one number.
-   It contains at least one special character from this set:  `!`,  `@`,  `#`,  `$`,  `%`,  `^`,  `&`, or  `*`.

Return  `"weak"`  if the password meets fewer than two of the rules. Return  `"medium"`  if the password meets 2 or 3 of the rules. Return  `"strong"`  if the password meets all 4 rules.


## My Thoughts
This was a relatively easy problem, however I knew I could of done the problem in less code. That would however require looping through the password multiple times, this wouldn't be a problem as a password wouldn't have been very long, but I wanted to optimize this a little bit for fun. I had all the requirements as a bool; then in one pass if the requirement was filled the boolean would change.

## Solution (Python)
```python
def check_strength(password):	
	has_upper = has_lower = has_digit = has_special = False
	special_chars = set("!@#$%^&*")

	for ch in password:
		if ch.isupper():
			has_upper = True
		elif ch.islower():
			has_lower = True
		elif ch.isdigit():
			has_digit = True
		elif ch in special_chars:
			has_special = True

	rule_count = 0

	if  len(password) >= 8:
		rule_count += 1
	if has_upper and has_lower:
		rule_count += 1
	if has_digit:
		rule_count += 1
	if has_special:
		rule_count += 1
	
	if rule_count == 4:
		return  "strong"
	elif rule_count >= 2:
		return  "medium"
	else:
		return  "weak"
```

