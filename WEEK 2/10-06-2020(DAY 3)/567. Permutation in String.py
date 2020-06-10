# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

s1 = "ab" 
s2 = "eidbaooo"
from itertools import permutations
lis_s1=[]
for i in permutations(s1):
    lis_s1.append(''.join(i))
for i in lis_s1:
    if(i in s2):
        print(True)
print(False)