
# Free Shipping
## Prompt
Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.

The given array will contain items from the list below:

Item	Price
"shirt"	34.25
"jeans"	48.50
"shoes"	75.00
"hat"	19.95
"socks"	15.00
"jacket"	109.95


## My Thoughts
To start with the problem I created a map. We then iterate through the given list, and add up to the total price and check if its atleast the price of the minimum for free shipping.

## Solution (Python)
```python
def gets_free_shipping(cart, minimum):
    items = {
        "shirt" : 34.25, 
        "jeans" : 48.50,
        "shoes" : 75.00,
        "hat"   : 19.95,
        "socks" : 15.00,
        "jacket": 109.95
    }

    total = 0

    for item in cart:
        total += items[item] 

    return total >= minimum
```
