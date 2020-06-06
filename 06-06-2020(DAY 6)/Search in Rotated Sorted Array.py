nums = [4,5,6,7,0,1,2]
target = 0
nums.sort()
low=0
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if(nums[mid]<target):
        low=mid+1
    elif(nums[mid]>target):
        high=mid-1
    else:
        print(mid)

print(-1)
