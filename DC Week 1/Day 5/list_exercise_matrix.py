matrix_1 = [[1,3], [2,4]]
matrix_2 = [[5,2], [1,0]]
matrix_3 = []
matrix_4 = []

for element in range(0, len(matrix_1)):
    matrix_3.append(matrix_1[0][element] + matrix_2[0][element])
    matrix_4.append(matrix_1[1][element] + matrix_2[1][element])
print(matrix_3 + matrix_4)
# matrix_4 = [(matrix_3[0][0] + matrix_3[0][2]),(matrix_3[0][1] + matrix_3[0][3]),(matrix_3[1][0] + matrix_3[1][2]),(matrix_3[1][1] + matrix_3[1][3])]
# There has to be a simpler way to solve this, ask in class

# print(matrix_4)