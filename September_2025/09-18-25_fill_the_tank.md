


# Fill the Tank

## Prompt

Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

-   `tankSize`  is the total capacity of the tank in gallons.
-   `fuelLevel`  is the current amount of fuel in the tank in gallons.
-   `pricePerGallon`  is the cost of one gallon of fuel.
-   The returned value should be rounded to two decimal places in the format:  `"$d.dd"`.

`cost_to_fill(20, 0, 4.00)`  should return  `"$80.00"`.
    
`cost_to_fill(15, 10, 3.50)`  should return  `"$17.50"`.
    
`cost_to_fill(18, 9, 3.25)`  should return  `"$29.25"`.
    
`cost_to_fill(12, 12, 4.99)`  should return  `"$0.00"`.
    
`cost_to_fill(15, 9.5, 3.98)`  should return  `"$21.89"`.

## My Thoughts
Super easy problem, just subtract tank size by current size and multiply it by the price per gallon. Then we just round to 2 digits.

## Solution (Python)
```python
def cost_to_fill(tank_size, fuel_level, price_per_gallon):
	fuel = tank_size - fuel_level
	result = fuel * price_per_gallon
	return f'${result:.2f}'
```
