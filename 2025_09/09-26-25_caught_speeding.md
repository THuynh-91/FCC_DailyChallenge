

# Caught Speeding
## Prompt


Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

-   If there were no vehicles speeding, return  `[0, 0]`.

`speeding([50, 60, 55], 60)`  should return  `[0, 0]`.
    
`speeding([58, 50, 60, 55], 55)`  should return  `[2, 4]`.
    
`speeding([61, 81, 74, 88, 65, 71, 68], 70)`  should return  `[4, 8.5]`.
    
`speeding([100, 105, 95, 102], 100)`  should return  `[2, 3.5]`.
    
`speeding([40, 45, 44, 50, 112, 39], 55)`  should return  `[1, 57]`.


## My Thoughts
This didn't require too much thinking. All I had to do was find the speeds that went above the limit. From that I found the difference of the speeds of the limit. I then divided by the length of the speeding limits. However if the len was 0 the avg speed was also 0 to avoid 0 division error.


## Solution (Python)
```python
def speeding(speeds, limit):
	speeding = []
	avg_speeding = 0
	for speed in speeds:
		if speed > limit:
			speeding.append(speed)
			
	for speed in speeding:
		avg_speeding += speed - limit
		
	if  not  len(speeding):
		avg_speeding = 0
	else:
		avg_speeding /= len(speeding)

	return  [len(speeding), avg_speeding]

```
