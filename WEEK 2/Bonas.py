tcs=int(input())
for tc in range(tcs):
    n=int(input())
    lis=[]
    for i in range(0,n+1):
        lis.append(True)
    p=2
    while(p*p<=n):
        if(lis[p]==True):
            for i in range(p * p, n+1, p): 
                    lis[i] = False
        p+=1
    for p in range(2,n+1):
        if(lis[p]):
            print(p,end=' ')