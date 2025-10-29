

#  Email Sorter
## Prompt

On October 29, 1971, the first email ever was sent, introducing the  `username@domain`  format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the  `@`), and username second (the part before the  `@`).

-   Sorting should be case-insensitive.
-   If more than one email has the same domain, sort them by their username.
-   Return an array of the sorted addresses.
-   Returned addresses should retain their original case.

For example, given  `["jill@mail.com", "john@example.com", "jane@example.com"]`, return  `["jane@example.com", "john@example.com", "jill@mail.com"]`.

## My Thoughts
Each address is split at the `@`.  The `sorted` call looks first at the part **after** the `@` (the domain), and if those match, at the part **before** it (the username).  Both are compared in lowercase so sorting ignores case, but the original strings are returned unchanged.

## Solution (Python)
```python
def sort(emails):
	return  sorted(emails, key=lambda e:  (
		e.split('@')[1].lower(),
		e.split('@')[0].lower()
	))
```

