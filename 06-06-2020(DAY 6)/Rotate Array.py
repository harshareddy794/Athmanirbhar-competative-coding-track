arr = [-1,-100,3,99] 
k = 2
for i in range(k):
    temp=arr[len(arr)-1]
    n=len(arr)-1
    for i in range(len(arr)-1):
        arr[n-i]=arr[n-i-1]
    arr[0]=temp