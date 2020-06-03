matrix = [
    [11,74,0,93],
    [40,11,74,7]
]
a=[]
for i in range(len(matrix)):
    for j in range(0,len(matrix[i])):
        if(i==j):
            a.append(matrix[i][j])
element=a[0]
for i in a:
    if(element!=i):
        print(False)
        break
else:
    print(True)
