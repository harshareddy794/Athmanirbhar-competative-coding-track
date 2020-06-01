# Solution for Leet code problem
# Problem url https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

nums = [8,1,2,2,3]
ans=[]
for i in range(0,len(nums)):
    smaller=0
    for j in range(0,len(nums)):
        if(nums[i]>nums[j]):
            smaller=smaller+1
    ans.append(smaller)
print(ans)