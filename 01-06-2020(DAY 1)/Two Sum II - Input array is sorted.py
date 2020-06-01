# Solution for Leet code problem
# Problem url https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

numbers = [2,7,11,15]
target = 9
for i in range(0,len(numbers)):
    for j in range(len(numbers)-1,i,-1):
        if(target==numbers[i]+numbers[j]):
            print(i+1,j+1)
