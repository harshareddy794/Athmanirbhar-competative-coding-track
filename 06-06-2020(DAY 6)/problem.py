# given an array example ar= {1,2,3,4,5} of size n  and q set of queries and x for each q. 
# Queries can be of two types    1 - left rotate array by x times   2 - right rotate array by x times   
# return the array after perfroming q set of queries      
# Sample case 1:   
# ar = { 4,7,9,0,4}   
# q=3   
# 1 3   2 8   1 9   2 2   1 2   
# Ans : {4,4,7,9,0}  

arr=[4,7,9,0,4]
q=int(input())
query=list(map(int,'1 3   2 20   1 9   2 2   1 2'.split()))
dict_query={}
for i in range(0,len(query),2):
    dict_query[query[i]]=dict_query.get(query[i],0)+query[i+1]
ans=(dict_query[1]-dict_query[2])
print(ans)
if(ans>0):
    for i in range(0,ans):
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[len(arr)-1]=temp
    print(arr)
else:
    for i in range(0,-ans):
        temp=arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
    print(arr)