from numpy import mat


raws=int(input("Enter the number of raws: "))
columns=int(input("Enter the number of columns: "))
matrix=[]
for i in range(raws):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(int(input("Enter a number: ")))
#print the matrix
for i in range(raws):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()
#print the sum of the matrix
print("The sum of the matrix is: ",sum(matrix[i][j] for i in range(raws) for j in range(columns)))
#print the average of the matrix
average=sum/(raws*columns)
print("The average of the matrix is: ",average)
#print the maximum of the matrix
maximum=matrix[0][0]
for i in range(raws):
    for j in range(columns):
        if maximum<matrix[i][j]:
            maximum=matrix[i][j]
print("The maximum of the matrix is: ",maximum)