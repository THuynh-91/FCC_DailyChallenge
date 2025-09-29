

# CSV Header Parser
## Prompt
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

-   The first line of a CSV file contains headings separated by commas.
-   Remove any leading or trailing whitespace from each heading.

`get_headings("name,age,city")`  should return  `["name", "age", "city"]`.
    
`get_headings("first name,last name,phone")`  should return  `["first name", "last name", "phone"]`.
    
`get_headings("username , email , signup date ")`  should return  `["username", "email", "signup date"]`.


## My Thoughts
Pretty simple solution. I just had to separate by commas. Iterate through the new array and remove trailing white spaces.


## Solution (Python)
```python
def get_headings(csv):
	fmat_csv = csv.split(",")
	return  [i.strip()  for i in fmat_csv]

```
