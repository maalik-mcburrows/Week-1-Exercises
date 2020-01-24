matrix_1 = [[1,3,9], [2,4,8]]
matrix_2 = [[5,2,3], [1,0,5]]
matrix_3 = []
matrix_4 = []

for element in (0, len(matrix_1)):
    matrix_3.append(matrix_1[0][element] + matrix_2[0][element])
    matrix_4.append(matrix_1[1][element] + matrix_2[1][element])
print(matrix_3 + matrix_4)

# No idea how to solve this shit ask in class

