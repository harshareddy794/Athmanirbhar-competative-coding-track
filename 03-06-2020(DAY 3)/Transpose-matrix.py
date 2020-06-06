# Output: [[1,4,7],[2,5,8],[3,6,9]]
arr=[[1,2,3],[4,5,6],[7,8,9]]
ans=[]
pos=0
for i in range(len(arr[0])):
    lis=[]
    for j in arr:
        lis.append(j[pos])
    ans.append(lis)
    pos+=1
print(ans)