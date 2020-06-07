# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
nums=[3,1,4,1,5]

k=2
count=0
for i in range(0,len(nums)): 
    for j in range(i+1,len(nums)) : 
        if nums[i] - nums[j] == k or nums[j] - nums[i] == k: 
            count += 1
                  
print(count) 