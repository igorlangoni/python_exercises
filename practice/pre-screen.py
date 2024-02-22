def solution(directions):
    clean_dir = ''
    for letter in directions:
        if letter in "FLR":
            clean_dir += letter
    # which dir robot is facing: 0 : right, 1: down, 2: left, 3: up
    facing = 0
    x = 0
    y = 0
    for letter in clean_dir:
        if letter == 'F':
            if facing == 0:
                x += 1
            elif facing == 1:
                y -= 1
            elif facing == 2:
                x -= 1
            elif facing == 3:
                y += 1
        if letter == 'R':
            if facing == 3:
                facing = 0
            else:
                facing += 1
        if letter == 'L':
            if facing == 0:
                facing = 3
            else:
                facing -= 1
    moves = 0
    if x < 0:
        if y > 0:
            if facing == 0 or facing == 1:
                moves += 1
            if facing == 2 or facing == 3:
                moves += 2
        if y < 0:
            if facing == 0 or facing == 3:
                moves += 1
            if facing == 2 or facing == 1:
                moves += 2
        if y == 0:
            if facing == 2:
                moves += 2
            if facing == 1 or facing == 3:
                moves += 1
            
    if x > 0:
        if y > 0:
            if facing == 2 or facing == 1:
                moves += 1
            if facing == 0 or facing == 3:
                moves += 2 
        if y < 0:
            if facing == 2 or facing == 3:
                moves += 1
            if facing == 0 or facing == 1:
                moves += 2
        if y == 0:
            if facing == 0:
                moves += 2
            if facing == 1 or facing == 3:
                moves += 1
    if x == 0:
        if y > 0:
            if facing == 3:
                moves += 2
            if facing == 0 or facing == 2:
                moves += 1
        if y < 0:
            if facing == 1:
                moves += 2
            if facing == 0 or facing == 2:
                moves += 1
                
    moves += (abs(int(x))+abs(int(y)))
            
    return moves


path = ['RFLFLFRFFFLF']