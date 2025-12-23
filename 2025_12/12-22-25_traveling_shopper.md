


# Traveling Shopper
## Prompt

Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

-   The given amount will be in the format  `["Amount", "Currency Code"]`. For example:  `["150.00", "USD"]`  or  `["6000", "JPY"]`.
-   Each array item you want to purchase will be in the same format.

-   If you can afford all the items in the list, return  `"Buy them all!"`.
-   Otherwise, return  `"Buy the first X items."`, where  `X`  is the number of items you can afford when purchased in the order given.

## My Thoughts
The first thing that is done is a dictionary that tells you how much a unit of a currency is worth in USD. From that we convert money into USD and convert it to a float as the input is a string. We then buy the items in order, we check if we can afford it, if we can afford it all, we buy it all. 

## Solution (Python)
```python
def buy_items(money, items):
	rates = {
		"USD":  1.00,
		"EUR":  1.10,
		"GBP":  1.25,
		"JPY":  0.0070,
		"CAD":  0.75
	}

	balance = float(money[0]) * rates[money[1]]
	count = 0

	for price, currency in items:
		cost = float(price) * rates[currency]

		if balance >= cost:
			balance -= cost	
			count += 1
		else:
			break

	if count == len(items):
		return  "Buy them all!"
	else:
		return f"Buy the first {count} items."
```
