# Solution for leetcode problem 
# Problem URL https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
nve=0
for i in grid:
    for j in i:
        if(j<0):
            nve=nve+1
print(nve)