

# Word Frequency
## Prompt


Given a paragraph, return an array of the three most frequently occurring words.

-   Words in the paragraph will be separated by spaces.
-   Ignore case in the given paragraph. For example, treat  `Hello`  and  `hello`  as the same word.
-   Ignore punctuation in the given paragraph. Punctuation consists of commas (`,`), periods (`.`), and exclamation points (`!`).
-   The returned array should have all lowercase words.
-   The returned array should be in descending order with the most frequently occurring word first

`get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")`  should return  `["coding", "python", "in"]`.
    
`get_words("I like coding. I like testing. I love debugging!")`  should return  `["i", "like", "coding"]`.

`get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!")`  should return  `["debug", "test", "deploy"]`.

## My Thoughts
For the solution my first initial thought was to use Counter, but I wasn't sure on how to remove the punctuations. I then noticed that most punctuations follow right after the end of a string. <br>
`end. but, Wow!`

Therefore in my solution I used `isalpha()` to check if the string had a punctuation and removed the last index of that string. Then used Counter to return the most common 3. This could be further improved, but for the current situation it is fine. 


## Solution (Python)
```python
from collections import Counter

def get_words(paragraph):
	new_lst = []
	word_splt = paragraph.lower().split(" ")

	for word in word_splt:
		if  not word.isalpha():
			new_lst.append(word[:-1])
		else:
			new_lst.append(word)
	top_words = [word for word,count in Counter(new_lst).most_common(3)]
	return top_words
```
