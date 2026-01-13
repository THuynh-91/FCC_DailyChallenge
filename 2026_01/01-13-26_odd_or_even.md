# Odd or Even?
## Prompt

Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.

## My Thoughts
This is a relatively simple problem. We use the modulo function: `%`. We then check if dibisible by 2, if `True` then "Even" else "Odd".
## Solution (Python)
```python
def odd_or_even(n):
    res = ''
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
```
