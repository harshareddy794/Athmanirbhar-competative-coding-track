# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: 
# Output: ["e","l","l"]


A=["bella","label","roller"]
from collections import Counter
counts = Counter(A[0]) 
for word in A:
    counts &= Counter(word)
print(counts)
res = []
for letter, count in counts.items():
    res += [letter] * count
    print(letter,count,res)
print(res)