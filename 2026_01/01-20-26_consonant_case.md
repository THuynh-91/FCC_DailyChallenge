
# Free Shipping
## Prompt
Given a string representing a variable name, convert it to consonant case using the following rules:

All consonants should be converted to uppercase.
All vowels (a, e, i, o, u in any case) should be converted to lowercase.
All hyphens (-) should be converted to underscores (_).
"Equal" if both used the same amount of energy.

## My Thoughts
I first took care of the vowels, we wanted to return the uppercase of the initial string, however wanted to keep any vowels lowercase. We also wanted to substitute hyphens for underscore.
To do this we iterate through the capitlized version of the given input, then prep for conditions.

## Solution (Python)
```python
def to_consonant_case(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    res = ''

    for c in s.upper():
        if c in vowels:
            res += c.lower()
        elif c == '-':
            res += '_'
        else:
            res += c

    return res
```
