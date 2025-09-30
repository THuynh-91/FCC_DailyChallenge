

# Photo Storage
## Prompt

Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:

-   1 gigabyte equals 1000 megabytes.
-   Return the number of whole photos the drive can store.

`number_of_photos(1, 1)`  should return  `1000`.
    
`number_of_photos(2, 1)`  should return  `500`.
    
`number_of_photos(4, 256)`  should return  `64000`.
    
`number_of_photos(3.5, 750)`  should return  `214285`.
    
`number_of_photos(3.5, 5.5)`  should return  `1571`.

## My Thoughts
That's all there is to it. Divide the total space by storage per photo using floor division. 


## Solution (Python)
```python
def number_of_photos(photo_size_mb, drive_size_gb):
	return drive_size_gb * 1000 // photo_size_mb
```
