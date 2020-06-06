tcs=int(input())
for tc in range(tcs):
    n=int(input())
    arr=list(map(int,(input().split())))
    lis=[]
    for number in arr:
        number=str(number)
        lis.append([char for char in number])
    ans=set()
    for i in lis:
        for j in range(len(i)):
            ans.add(int(i[j]))
    print(sorted(ans))
    