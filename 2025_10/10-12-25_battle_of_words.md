

#  Battle of Words
## Prompt

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

-   The given sentences will always contain the same number of words.
-   Words are separated by a single space and will only contain letters.
-   The value of each word is the sum of its letters.
-   Letters  `a`  to  `z`  correspond to the values  `1`  through  `26`. For example,  `a`  is  `1`, and  `z`  is  `26`.
-   A capital letter doubles the value of the letter. For example,  `A`  is  `2`, and  `Z`  is  `52`.
-   Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
-   A word wins if its value is greater than the opposing word's value.
-   The team with more winning words is the winner.

Return  `"We win"`  if your team is the winner,  `"We lose"`  if your team loses, and  `"Draw"`  if both teams have the same number of wins.

## My Thoughts
This was a reallyy interesting problem. I just mapped the letters a-z onto 1...26 using their positions int he alphabet. If the letter was an uppercase just **double** it's value. I then split both sentences on spaces and compared words positionally. 

## Solution (Python)
```python
	def battle(ours:  str, theirs:  str) -> str:
		def word_value(w:  str) -> int:
			total = 0
			for ch in w:
				base = ord(ch.lower()) - 96
				total += base * (2  if ch.isupper()  else  1)
			return total

		aw = bw = 0

		for a, b in  zip(ours.split(), theirs.split()):
			va, vb = word_value(a), word_value(b)
			if va > vb:
				aw += 1
			elif vb > va:
				bw += 1

		if aw > bw:
			return  "We win"
		if bw > aw:
			return  "We lose"
		return  "Draw"
```

