raw=int(input("Enter a number: "))
column=int(input("Enter a number: "))
matrix=[]
for i in range(raw):
    matrix.append([])
    for j in range(column):
        matrix[i].append(int(input("enter the nuber: ")))
#print the matrix
for i in range(raw):
    for j in range(column):
        print(matrix[i][j],end=" ")
    print()