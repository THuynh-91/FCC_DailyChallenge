
# Class Average
## Prompt
Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:

Average Score	Letter Grade
97-100	"A+" <br>
93-96	"A"<br>
90-92	"A−"<br>
87-89	"B+"<br>
83-86	"B"<br>
80-82	"B-"<br>
77-79	"C+"<br>
73–76	"C"<br>
70-72	"C-"<br>
67-69	"D+"<br>
63-66	"D"<br>
60–62	"D-"<br>
below 60	"F"<br>
Calculate the average by adding all scores in the array and dividing by the total number of scores.

## My Thoughts
The solution was super simple, generate the average score from the given list, then return the average given the table provided.

## Solution (Python)
```python
def get_average_grade(scores):
    avg = sum(scores) / len(scores)

    if 97 <= avg <= 100:
        return "A+"
    elif 93 <= avg < 97:
        return "A"
    elif 90 <= avg < 93:
        return "A-"
    elif 87 <= avg < 90:
        return "B+"
    elif 83 <= avg < 87:
        return "B"
    elif 80 <= avg < 83:
        return "B-"
    elif 77 <= avg < 80:
        return "C+"
    elif 73 <= avg < 77:
        return "C"
    elif 70 <= avg < 73:
        return "C-"
    elif 67 <= avg < 70:
        return "D+"
    elif 63 <= avg < 67:
        return "D"
    elif 60 <= avg < 63:
        return "D-"
    else:
        return "F"
```
