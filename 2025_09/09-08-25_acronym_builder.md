


# Acronym Builder

## Prompt
Given a string containing one or more words, return an acronym of the words using the following constraints:

-   The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
-   The acronym should ignore the first letter of these words unless they are the first word of the given string:  `a`,  `for`,  `an`,  `and`,  `by`, and  `of`.
-   The acronym letters should be returned in order they are given.
-   The acronym should not contain any spaces.

`build_acronym("Search Engine Optimization")`  should return  `"SEO"`.
    
`build_acronym("Frequently Asked Questions")`  should return  `"FAQ"`.
    
`build_acronym("National Aeronautics and Space Administration")`  should return  `"NASA"`.
    
`build_acronym("Federal Bureau of Investigation")`  should return  `"FBI"`.
    
  `build_acronym("For your information")`  should return  `"FYI"`.
    
`build_acronym("By the way")`  should return  `"BTW"`.


## My Thoughts
This was surprisingly quite easy. I had to make a list of avoided words: `avoid = ['a', 'for', 'an', 'and', 'by', 'of']`. I made a list of the string, and grabbed the first letter in each item of the list.

## Solution (Python)
```python
def  build_acronym(s): 
	avoid = ['a', 'for', 'an', 'and', 'by', 'of'] 
	
	list_s = s.split(" ") 
	result = ""  
	
	for item in list_s: 
		if item not  in avoid: 
			result += item[0].upper() 
	return result
```
