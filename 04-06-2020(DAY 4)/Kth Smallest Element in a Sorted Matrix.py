matrix = [[1,2],[1,3]]
k = 2
all_lis=[]
for i in matrix:
    for j in i:
        all_lis.append(j)
print(sorted(all_lis)[k-1])