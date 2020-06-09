# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

matrix=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

x=len(matrix[0])
y=len(matrix)
ans=[]
for i in range(0,x):
    ans.append(matrix[0][i])
for i in range(0,y):
    ans.append(matrix[i][x-1])
for i in range(x-1,0-1,-1):
    ans.append(matrix[y-1][i])
for i in range(y-1,0,-1):
    ans.append(matrix[i][0])
for i in range(y-1,0,-1):
    ans.append(matrix[i][0])
print(list(set(ans)))