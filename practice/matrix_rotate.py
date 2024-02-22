# Rotate Matrix 90 degrees clockwise
def rotate_90_cw(matrix):
    new_mat = []
    row = len(matrix)-1
    while row>=0:
        for col in range(0, len(matrix)):
            if (len(new_mat) < (col+1)):
                new_mat.append([matrix[row][col]])
            else:
                new_mat[col].append(matrix[row][col])
        row -= 1
    return new_mat

# Rotate Matrix Counter-Clockwise
def rotate_90_ccw(matrix, n):
    new_matrix = []
    row = 0
    while row<len(matrix):
        r = 0
        for col in range(len(matrix)-1, -1, -1):
            if (len(new_matrix) < len(matrix)):
                new_matrix.append([matrix[row][col]])
            else:
                new_matrix[r].append(matrix[row][col])
                r += 1
        row += 1
    return new_matrix

matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix2 =   [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]