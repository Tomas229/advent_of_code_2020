import copy
with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
        input_file[i] = list(input_file[i])

    # print(input_file)


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1, j))
    if i+1 < m:
        adjacent_indices.append((i+1, j))
    if j > 0:
        adjacent_indices.append((i, j-1))
    if j+1 < n:
        adjacent_indices.append((i, j+1))
    if i > 0 and j > 0:
        adjacent_indices.append((i-1, j-1))
    if i > 0 and j + 1 < n:
        adjacent_indices.append((i-1, j+1))
    if i+1 < m and j + 1 < n:
        adjacent_indices.append((i+1, j+1))
    if i+1 < m and j > 0:
        adjacent_indices.append((i+1, j-1))
    return adjacent_indices


def equilibrium(l):
    x = len(l)
    y = len(l[0])
    new = copy.deepcopy(l)
    while True:
        l = copy.deepcopy(new)
        for i in range(x):
            for j in range(y):
                adj = get_adjacent_indices(i, j, x, y)
                hash_count = 0
                for a in adj:
                    if l[a[0]][a[1]] == "#":
                        hash_count += 1
                if l[i][j] == "L" and hash_count == 0:
                    new[i][j] = "#"
                if l[i][j] == "#" and hash_count > 3:
                    new[i][j] = "L"
        if(new == l):
            break
    count = 0
    for i in range(x):
        for j in range(y):
            if l[i][j] == "#":
                count += 1
    return count


print(equilibrium([list("L.LL.LL.LL"),
                   list("LLLLLLL.LL"),
                   list("L.L.L..L.."),
                   list("LLLL.LL.LL"),
                   list("L.LL.LL.LL"),
                   list("L.LLLLL.LL"),
                   list("..L.L....."),
                   list("LLLLLLLLLL"),
                   list("L.LLLLLL.L"),
                   list("L.LLLLL.LL")]))

# print(equilibrium(input_file))
# 1:30


def get_adjacent_indices2(i, j, l):
    adjacent_indices = []
    len_x = len(l)
    len_y = len(l[0])
    x = i
    y = j
    while(x + 1 < len_x):
        x += 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while x > 0:
        x -= 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while(y + 1 < len_y):
        y += 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while y > 0:
        y -= 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while(x + 1 < len_x and y + 1 < len_y):
        x += 1
        y += 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while(x + 1 < len_x and y > 0):
        x += 1
        y -= 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while(x > 0 and y > 0):
        x -= 1
        y -= 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break
    x = i
    y = j
    while(x > 0 and y + 1 < len_y):
        x -= 1
        y += 1
        if(l[x][y] != "."):
            adjacent_indices.append((x, y))
            break

    return adjacent_indices


def equilibrium2(l):
    x = len(l)
    y = len(l[0])
    new = copy.deepcopy(l)
    while True:
        l = copy.deepcopy(new)
        for i in range(x):
            for j in range(y):
                adj = get_adjacent_indices2(i, j, l)
                hash_count = 0
                for a in adj:
                    if l[a[0]][a[1]] == "#":
                        hash_count += 1
                if l[i][j] == "L" and hash_count == 0:
                    new[i][j] = "#"
                if l[i][j] == "#" and hash_count > 4:
                    new[i][j] = "L"
        if(new == l):
            break
    count = 0
    for i in range(x):
        for j in range(y):
            if l[i][j] == "#":
                count += 1
    return count


print(equilibrium2([list("L.LL.LL.LL"),
                    list("LLLLLLL.LL"),
                    list("L.L.L..L.."),
                    list("LLLL.LL.LL"),
                    list("L.LL.LL.LL"),
                    list("L.LLLLL.LL"),
                    list("..L.L....."),
                    list("LLLLLLLLLL"),
                    list("L.LLLLLL.L"),
                    list("L.LLLLL.LL")]))
print(equilibrium2(input_file))

#40 minsz