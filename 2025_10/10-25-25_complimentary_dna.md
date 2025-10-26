

#  Complimentary DNA
## Prompt


Given a string representing a DNA sequence, return its complementary strand using the following rules:

-   DNA consists of the letters  `"A"`,  `"C"`,  `"G"`, and  `"T"`.
-   The letters  `"A"`  and  `"T"`  complement each other.
-   The letters  `"C"`  and  `"G"`  complement each other.

For example, given  `"ACGT"`, return  `"TGCA"`.

## My Thoughts
Just build the complimentary string in the DNA string.

## Solution (Python)
```python
def complementary_dna(dna):
	comp = {"A":  "T",  "T":  "A",  "C":  "G",  "G":  "C"}
	return  "".join(comp[n]  for n in dna)

```

