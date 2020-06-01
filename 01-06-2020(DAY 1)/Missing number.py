# Solution for geeks for geeks problem
# Problem url https://practice.geeksforgeeks.org/problems/missing-number/0

# My code
tcs=int(input())
for tc in range(0,tcs):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    n=n-1
    for i in range(0,n):
        if(arr[i]!=i+1):
            print(i+1)
            break

#Editorial Solution
tcs=int(input())
for tc in range(0,tcs):
    n=int(input())
    arr=list(map(int,input().split()))
    tot=(n*(n+1))/2
    sm=sum(arr)
    print(int(tot-sm))