# Vowel Balance

## Prompt
Given a string, determine whether the number of vowels in the first half of the string equals the number of vowels in the second half.  
- Consider vowels: `a, e, i, o, u` (case-insensitive).  
- If the length is odd, ignore the middle character.  
- The string may contain any characters.

## My Thoughts
My first idea was to branch on odd/even lengths and slice differently, but that felt messy.  
Noticing that floor division already gives the correct split point, we can use:
- `left = s[: n // 2]`
- `right = s[(n + 1) // 2 :]`  

This ignores the middle char when `n` is odd because `(n + 1) // 2` is the first index *after* the middle.  
Example: `4//2 == 2` and `5//2 == 2`, so the left half is consistent; the right half naturally skips the center when needed.

We then compare vowel counts in `left` vs `right`.

## Solution (Python)
```python
def is_balanced(s: str) -> bool:
    s = s.lower()
    vowels = "aeiou"
    left = s[: len(s) // 2]
    right = s[(len(s) + 1) // 2 :]
    return sum(c in vowels for c in left) == sum(c in vowels for c in right)
