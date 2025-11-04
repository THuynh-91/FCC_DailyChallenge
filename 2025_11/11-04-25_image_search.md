

#  Image Search
## Prompt

On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

-   Ignore the case when matching the search terms.
-   Return the images in the same order they appear in the input array.

## My Thoughts
If the term was is in the string of the image, then the image would be appended to the result. I also had to make sure the term and list items were universal so I made them `lower()`.

## Solution (Python)
```python
def image_search(images, term):
	res = []
	for image in images:
		if term.lower()  in image.lower():
			res.append(image)
	return res
```

