

# Longest Word
## Prompt


Given a sentence, return the longest word in the sentence.

-   Ignore periods (`.`) when determining word length.
-   If multiple words are ties for the longest, return the first one that occurs.

`get_longest_word("coding is fun")`  should return  `"coding"`.
    
`get_longest_word("Coding challenges are fun and educational.")`  should return  `"educational"`.
    
`get_longest_word("This sentence has multiple long words.")`  should return  `"sentence"`.


## My Thoughts
This was a fun challenge. There were a couple of ways I thought about going through this. I thought about using zip, or just finding the longest word in the sentence using a max and iterating through everything. However I wanted to use enumerate. From this I just iterated through the text, had the longest be a tuple of the length and the word. After iterating through the list once it returns the longest word given the index. Now that I think about it. I can just store the word itself and not the index.

## Solution (Python)
```python
def get_longest_word(sentence):
	res = sentence.replace(".",  "").split()
	longest = (0,0)

	for index, word in  enumerate(res):
		if  len(word) > longest[0]:
		longest = (len(word), index)
	return res[longest[1]]
```
## UPDATED (Python)

```python
def get_longest_word(sentence):
	res = sentence.replace(".",  "").split()
	longest = (0,"")
	
	for index, word in  enumerate(res):
		if  len(word) > longest[0]:
		longest = (len(word), word)
	return longest[1]
```
