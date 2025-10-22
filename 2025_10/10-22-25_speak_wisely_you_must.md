

#  Speak Wisely, You Must
## Prompt

Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

-   Words are separated by a single space.
-   Find the first occurrence of one of the following words in the sentence:  `"have"`,  `"must"`,  `"are"`,  `"will"`,  `"can"`.
-   Move all words before and including that word to the end of the sentence and:
    -   Preserve the order of the words when you move them.
    -   Make them all lowercase.
    -   And add a comma and space before them.
-   Capitalize the first letter of the new first word of the sentence.
-   All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
-   Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.

For example, given  `"You must speak wisely."`  return  `"Speak wisely, you must."`

## My Thoughts
The `wise_speak()` function takes a normal sentence and makes it sound like advice from a wise teacher. It looks for the first helper word such as “have,” “must,” “are,” “will,” or “can.” Then it moves all the words before and including that helper word to the end of the sentence, adds a comma before them, and keeps the punctuation at the end. The new first word is capitalized, and the moved words are made lowercase. For example, “You must speak wisely.” becomes “Speak wisely, you must.”

## Solution (Python)
```python
def wise_speak(sentence):
	keywords = ["have",  "must",  "are",  "will",  "can"]
	punctuation = sentence[-1]
	words = sentence[:-1].split()
	split_index = next((i for i, w in  enumerate(words)  if w.lower()  in keywords),  -1)

	if split_index == -1:
		return sentence

	before = words[:split_index + 1]
	after = words[split_index + 1:]

	new_first = " ".join(after).capitalize()
	new_second = " ".join(w.lower()  for w in before)
	result = f"{new_first}, {new_second}{punctuation}"

	return result

```

