
unique = [0,1,2]
matrix = [list() for x in range(len(unique))]
print(matrix)
for _ in range(len(unique)):
    matrix[_] = [0 for x in range(len(unique))]
print(matrix)
