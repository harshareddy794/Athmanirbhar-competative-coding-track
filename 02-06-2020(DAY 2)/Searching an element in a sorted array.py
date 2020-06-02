# Problem from geeks for geeks 
# Problem URL https://practice.geeksforgeeks.org/problems/who-will-win/0
tcs=int(input())
for tc in range(0,tcs):
    n=list(map(int,input().split()))[1]
    data=list(map(int,input().split()))
    if n in data:
        print(1)
    else:
        print(-1)