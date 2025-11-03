

#  Word Counter
## Prompt

Given a sentence string, return the number of words that are in the sentence.

## My Thoughts
This code does exactly that... it takes the sentence and splits it by white space into an array. You then just grab the length of said array.

## Solution (Python)
```python
def count_words(sentence):
	return  len(sentence.split())
```

