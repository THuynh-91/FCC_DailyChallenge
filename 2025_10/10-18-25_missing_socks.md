

#  Missing Socks
## Prompt

Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

-   Every 2 wash cycles, you lose a single sock.
-   Every 3 wash cycles, you find a single missing sock.
-   Every 5 wash cycles, a single sock is worn out and must be thrown away.
-   Every 10 wash cycles, you buy a pair of socks.
-   You can never have less than zero total socks.
-   Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
-   Return the number of complete pairs of socks.

## My Thoughts
You start with **pairs of socks**, but all the wash-cycle rules affect **individual socks**.  
So we first convert pairs → socks (`2 * pairs`).

Then each rule either adds or subtracts socks based on how many cycles you’ve completed.

## Solution (Python)
```python
def sock_pairs(p:  int, c:  int) -> int:
	socks = 2*p - (c//2) + (c//3) - (c//5) + 2*(c//10)
	socks = max(0, socks)
	return socks // 2
```

