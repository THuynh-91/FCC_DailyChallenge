
# Hex Validator
## Prompt
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

Start with a #, and
be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).

## My Thoughts
To solve this, we enforce the `#` at the start. I didn't want to use regex, therefore we enforce the exxact length of `3-6` chars after the `#`. Then we validate hex characters only.
We check for case insensitivty and reject spaces.

## Solution (Python)
```python
def is_valid_hex(s):
    if not s.startswith("#"):
        return False

    hex_part = s[1:]

    if len(hex_part) not in (3, 6):
        return False

    valid_chars = "0123456789abcdefABCDEF"

    for ch in hex_part:
        if ch not in valid_chars:
            return False

    return True

```
