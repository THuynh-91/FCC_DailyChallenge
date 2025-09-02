def is_balanced(s):

    s = s.lower()
    v = 'aeiou'


    lower = s[0:len(s)//2]
    upper = s[(len(s) +1)//2:]


    return sum(c in v for c in lower) == sum(c in v for c in upper)
  
print(is_balanced("racecar")) # -> True
