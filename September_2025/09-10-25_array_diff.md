

# Array Diff

## Prompt
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

-   The returned array should be sorted in alphabetical order

`array_diff(["apple", "banana"], ["apple", "banana", "cherry"])`  should return  `["cherry"]`.
    
`array_diff(["apple", "banana", "cherry"], ["apple", "banana"])`  should return  `["cherry"]`.
    
`array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])`  should return  `["eight", "four", "six", "two"]`.
    
`array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"])`  should return  `["five", "one", "seven", "three"]`.
    
  `array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"])`  should return  `["freeCodeCamp", "rocks"]`.


## My Thoughts
Honestly I overcomplicated this. I wanted to merge the two arrays then use set, but I remove that only removed duplicates. That means some of the items were not unique. From that I just decided to use combine the list, go to combine the list, and check if the item was unique to only one of the arrays.


## Solution (Python)
```python
def array_diff(arr1, arr2):
	combined_arr = list(set(arr1 + arr2))
	result = []

	for i in combined_arr:
		if i not in arr1 or i not  in arr2:
	result.append(i)
return  sorted(result)
```
