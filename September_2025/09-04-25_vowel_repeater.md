# Vowel Repeater

## Prompt



Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

-   The letters  `a`,  `e`,  `i`,  `o`, and  `u`, in either uppercase or lowercase, are considered vowels.
-   The original vowel should keeps its case.
-   Repeated vowels should be lowercase.
-   All non-vowel characters should keep their original case.

`repeat_vowels("hello world")`  should return  `"helloo wooorld"`.
    
`repeat_vowels("freeCodeCamp")`  should return  `"freeeCooodeeeeCaaaaamp"`.
    
`repeat_vowels("AEIOU")`  should return  `"AEeIiiOoooUuuuu"`.


## My Thoughts
The problem was so simple, my mind went through various routes and ended up overcomplicating it. My first thought was to declare my vowels: `v = 'aeiou'.` Secondly I thought it would be appropriate to iterate over the original string and use `replace` however this would cause a lot of errors. Then I tried brainstorming and just had an empty string. If the char was not a vowel append that that char. If it was the vowel append the original char (we needed to keep the original vowel in case if it was capitalized, the repeating vowels are all lowercase). After that I appended the `vowel * count`.

## Solution (Python)
```python
def repeat_vowels(s):
	v = 'aeiouAEIOU'
	count = 0
	result = ''
	for i in s:
		if i not  in v:
			result += i
		else:
			result += i + i.lower()*count
			count += 1
	return result
```
