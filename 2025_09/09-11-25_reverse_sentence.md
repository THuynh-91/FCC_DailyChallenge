

# Reverse Sentence

## Prompt

Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

-   In the given string, words can be separated by one or more spaces.
-   The returned string should only have one space between words.

`reverse_sentence("world hello")`  should return  `"hello world"`.
    
`reverse_sentence("push commit git")`  should return  `"git commit push"`.
    
`reverse_sentence("npm install apt sudo")`  should return  `"sudo apt install npm"`.
    
`reverse_sentence("import default function export")`  should return  `"export function default import"`.


## My Thoughts
Relatively easy problem. I just had to get rid of all the white spaces and turn the string into a list of words. Therefore the split function is extremely helpful. Then I just joined the  list of words in reverse order with a space separator.


## Solution (Python)
```python
def reverse_sentence(sentence):
	lst_sentence = sentence.split()
	return  " ".join(lst_sentence[::-1])
```
