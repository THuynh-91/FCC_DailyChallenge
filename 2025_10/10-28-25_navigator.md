

#  Navigator
## Prompt
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

-   You always start on the  `"Home"`  page, which will not be included in the commands array.
-   Valid commands are:
    -   `"Visit Page"`: Where  `"Page"`  is the name of the page you are visiting. For example,  `"Visit About"`  takes you to the  `"About"`  page. When you visit a new page, make sure to discard any forward history you have.
    -   `"Back"`: Takes you to the previous page in your history or stays on the current page if there isn't one.
    -   `"Forward"`: Takes you forward in the history to the page you came from or stays on the current page if there isn't one.

For example, given  `["Visit About Us", "Back", "Forward"]`, return  `"About Us"`.

## My Thoughts
I built a simple browser history simulator using two stacks — one for back history and one for forward history. Each "Visit" command pushes the current page to the back stack and clears forward history, while "Back" and "Forward" move pages between the stacks appropriately. Finally, the function returns the page you end up on after all commands are executed.

## Solution (Python)
```python
def navigate(commands):
	back_stack = []
	forward_stack = []
	current = "Home"

	for cmd in commands:
		if cmd.startswith("Visit "):
			page = cmd[6:]
			back_stack.append(current)
			current = page
			forward_stack.clear()
		elif cmd == "Back":
			if back_stack:
				forward_stack.append(current)
				current = back_stack.pop()
		elif cmd == "Forward":
			if forward_stack:
				back_stack.append(current)
				current = forward_stack.pop()
				
	return current
```

