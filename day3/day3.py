def slope(puzzle, right, down):
    length = len(puzzle)
    heigth = len(puzzle[0])

    x = 0
    y = 0
    count = 0
    while(x < length):
        if(puzzle[x][y] == "#"):
            count += 1
        x += down
        y = ((y + right) % heigth)
    return count


with open("puzzle.txt") as file:
    pass_file = file.readlines()
    for i in range(len(pass_file)):
        pass_file[i] = pass_file[i][0:-1]

    print(slope(pass_file, 3, 1))

    print(slope(pass_file, 1, 1)*slope(pass_file, 3, 1) *
          slope(pass_file, 5, 1)*slope(pass_file, 7, 1)*slope(pass_file, 1, 2))

# 28 mins first star 289
# 5 mins second star 5522401584
