def rotate_matrix_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix_90(matrix))  # [[7,4,1],[8,5,2],[9,6,3]]
