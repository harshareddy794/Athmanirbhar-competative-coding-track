# tcs=int(input())
# for tc in range(tcs):
n=int(input())
n=n+2
arr=list(map(int,input().split()))
repeated=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            repeated.append(arr[i])
for i in repeated:
    print(i,end=' ')