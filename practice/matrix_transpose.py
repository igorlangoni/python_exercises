# Transpose Matrix
def transpose(matrix):
    return list(map(list, zip(*mat)))


mat = [
        [7, 8],
        [9, 10],
		[11, 12]
]

print(transpose(mat))




