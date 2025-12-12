


# Inventory Update
## Prompt
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

-   Each element in the arrays will have the format:  `[quantity, "item"]`, where  `quantity`  is an integer and  `"item"`  is a string.
-   Update items in the inventory by adding the quantity of any matching items from the shipment.
-   If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
-   Return inventory in the order it was given with new items at the end in the order they appear in the shipment.

For example, given an inventory of  `[[2, "apples"], [5, "bananas"]]`  and a shipment of  `[[1, "apples"], [3, "bananas"]]`, return  `[[3, "apples"], [8, "bananas"]]`.
## My Thoughts
We first map the name it its index in the inventory. From that we process each shipment item.

## Solution (Python)
```python
def update_inventory(inventory, shipment):
	item_index = {}
	for i,  (qty, item)  in  enumerate(inventory):
		item_index[item] = i

	for qty, item in shipment:
		if item in item_index:
			inventory[item_index[item]][0] += qty
		else:
			inventory.append([qty, item])
			item_index[item] = len(inventory) - 1
	return inventory

```
