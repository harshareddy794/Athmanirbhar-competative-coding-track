tuple_data=[1,3,5,6],2
arr=(tuple_data[0])
n=tuple_data[1]
if(n in arr):
    print(arr.index(n))
else:
    if(arr[len(arr)-1]<n):
        print(len(arr))
    else:
        count=0
        for i in arr:
            if(i<n):
                count+=1
            else:
                print(count)
                break



        