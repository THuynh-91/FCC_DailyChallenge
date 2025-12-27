


# Rock,Paper,Scissors
## Prompt


Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

-   The input strings will always be  `"Rock"`,  `"Paper"`, or  `"Scissors"`.
-   `"Rock"`  beats  `"Scissors"`.
-   `"Paper"`  beats  `"Rock"`.
-   `"Scissors"`  beats  `"Paper"`.

Return:

-   `"Player 1 wins"`  if Player 1 wins.
-   `"Player 2 wins"`  if Player 2 wins.
-   `"Tie"`  if both players choose the same option.

## My Thoughts
I used a similar component in my rock-paper-scissors game. I had a counter dictionary that would map out its counter part. I used the same idea and mapped it out the possible scenarios. First if the cases were the same it was a tie. Then we checked if player 1 beat player 2, if not then the only possible choice left is that player 2 won. 

## Solution (Python)
```python
def rock_paper_scissors(player1, player2):
	counters = {
	'Rock':'Scissors',
	'Scissors':'Paper',
	'Paper':  'Rock'
	}

	if player1 == player2:
		return  "Tie"

	if counters[player1] == player2:
		return  'Player 1 wins'

	return  'Player 2 wins'
```
