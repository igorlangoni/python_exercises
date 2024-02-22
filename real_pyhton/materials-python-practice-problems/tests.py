import string

sud_grid = [
    [1,3,2,5,4,6,9,8,7], 
    [4,6,5,8,7,9,3,2,1], 
    [7,9,8,2,1,3,6,5,4], 
    [9,2,1,4,3,5,8,7,6], 
    [3,5,4,7,6,8,2,1,9], 
    [6,8,7,1,9,2,5,4,3], 
    [5,4,6,9,8,1,4,3,2], 
    [2,7,3,6,5,7,1,9,8], 
    [8,1,9,3,2,4,7,6,5]
]

possible_digits = string.digits[1:]
if len(sud_grid) != 9 or len(sud_grid[0]) != 9:
    print(False)
for i in range(9):
    for d in possible_digits:
        if sud_grid[i].count(d) > 1:
            print(False)
for j in range(9):
    seen = []
    for i in range(9):
        if sud_grid[i][j] not in seen and sud_grid[i][j] != '0':
            seen.append(sud_grid[i][j])
        elif sud_grid[i][j] in seen:
            print(False)
for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        seen = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                num = sud_grid[i+x][j+y]
                if num not in seen and num != "0":
                    seen.append(num)
                elif num in seen:
                    print(False)
print(True)
