

# File Storage
## Prompt


Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

-   The unit for the file size can be bytes (`"B"`), kilobytes (`"KB"`), or megabytes (`"MB"`).
-   Return the number of whole files the drive can fit.
-   Use the following conversions:

`number_of_files(500, "KB", 1)`  should return  `2000`.
    
`number_of_files(50000, "B", 1)`  should return  `20000`.
    
`number_of_files(5, "MB", 1)`  should return  `200`.
    
`number_of_files(4096, "B", 1.5)`  should return  `366210`.
    
 `number_of_files(220.5, "KB", 100)`  should return  `453514`.
    
`number_of_files(4.5, "MB", 750)`  should return  `166666`.

## My Thoughts
I had all the sizes converted to Bytes, then just floor divided.


## Solution (Python)
```python
def number_of_files(file_size, file_unit, drive_size_gb):
	sizes = {
		"B":  1,
		"KB":  1000,
		"MB":  1000000,
		"GB":  1000000000
		}
	return drive_size_gb * sizes["GB"] // (file_size * sizes[file_unit])
```
