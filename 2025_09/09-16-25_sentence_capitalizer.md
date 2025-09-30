

# Sentence Capitalizer
## Prompt


Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

-   All other characters should be preserved.
-   Sentences can end with a period (`.`), one or more question marks (`?`), or one or more exclamation points (`!`).

`capitalize("this is a simple sentence.")`  should return  `"This is a simple sentence."`.
    
`capitalize("hello world. how are you?")`  should return  `"Hello world. How are you?"`.
    
`capitalize("i did today's coding challenge... it was fun!!")`  should return  `"I did today's coding challenge... It was fun!!"`.
    
`capitalize("crazy!!!strange???unconventional...sentences.")`  should return  `"Crazy!!!Strange???Unconventional...Sentences."`.
    
`capitalize("there's a space before this period . why is there a space before that period ?")`  should return  `"There's a space before this period . Why is there a space before that period ?"`.

## My Thoughts
This was a bit more challenging because it didn't follow standard sentence structures. Additionally I couldn't check `isalpha()` as `it's` is a valid word not an end of a sentence. To complete this I had to set a checker to allow the next word to be capitalize through a Boolean only if the ending was met.


## Solution (Python)
```python
def capitalize(paragraph:  str) -> str:
	out = []
	cap_next = True
	for ch in paragraph:
		if cap_next and ch.isalpha():
			out.append(ch.upper())
			cap_next = False
		else:
			out.append(ch)
		if ch in  '.?!':
			cap_next = True
	return  ''.join(out)
```
