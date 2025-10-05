

#  Stellar Classification
## Prompt


October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

-   `"O"`: 30,000 K or higher
    
-   `"B"`: 10,000 K - 29,999 K
    
-   `"A"`: 7,500 K - 9,999 K
    
-   `"F"`: 6,000 K - 7,499 K
    
-   `"G"`: 5,200 K - 5,999 K
    
-   `"K"`: 3,700 K - 5,199 K
    
-   `"M"`: 0 K - 3,699 K
    
-   Return the classification of the given star.


## My Thoughts
Honestly... just check the requirements.

## Solution (Python)
```python
def classification(temp_k):
	if temp_k < 0:
		raise ValueError("Temperature must be non-negative (K).")
	if temp_k >= 30000:  return  "O"
	if temp_k >= 10000:  return  "B"
	if temp_k >= 7500:  return  "A"
	if temp_k >= 6000:  return  "F"
	if temp_k >= 5200:  return  "G"
	if temp_k >= 3700:  return  "K"
	return  "M"
```

