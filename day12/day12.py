import copy
with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)


def move(l):
    facing = 0
    x = 0
    y = 0

    for ins in l:
        action = ins[0]
        num = int(ins[1:])

        ret = move_aux(action, num, facing)

        x += ret[0]
        y += ret[1]
        facing = ret[2]

    res = abs(x) + abs(y)
    print(res)
    return res


def move_aux(action, num, face):
    x = 0
    y = 0
    if action == "N":
        y += num
    elif action == "S":
        y -= num
    elif action == "E":
        x += num
    elif action == "W":
        x -= num
    elif action == "F":
        ret = move_aux(degreesToCardinal(face), num, face)
        x += ret[0]
        y += ret[1]
    elif action == "L":
        face = (face + num) % 360
    elif action == "R":
        ret = move_aux("L", -num, face)
        face = ret[2]

    return x, y, face


def degreesToCardinal(degrees):
    if degrees == 0:
        return "E"
    elif degrees == 90:
        return "N"
    elif degrees == 180:
        return "W"
    elif degrees == 270:
        return "S"


move(["F10",
      "N3",
      "F7",
      "R90",
      "F11"])
move(input_file)

# Primera parte 25 mins


def move_2(l):
    x = 10
    y = 1

    sx = 0
    sy = 0

    for ins in l:
        action = ins[0]
        num = int(ins[1:])

        ret = move_aux_2(action, num, x, y)

        x += ret[0]
        y += ret[1]
        sx += ret[2]
        sy += ret[3]

    res = abs(sx) + abs(sy)
    print(res)
    return res


def move_aux_2(action, num, wx, wy):
    x = 0
    y = 0
    sx = 0
    sy = 0
    if action == "N":
        y += num
    elif action == "S":
        y -= num
    elif action == "E":
        x += num
    elif action == "W":
        x -= num

    elif action == "F":
        sx += wx * num
        sy += wy * num

    elif action == "L":
        ret = rotate(wx, wy, num)
        x = ret[0]-wx
        y = ret[1] - wy
    elif action == "R":
        ret = rotate(wx, wy, 360-num)
        x = ret[0] - wx
        y = ret[1] - wy

    return x, y, sx, sy


def rotate(x, y, degree):
    if degree == 90:
        return -y, x
    elif degree == 180:
        return -x, -y
    elif degree == 270:
        return y, -x
    elif degree == 0:
        return x, y


move_2(["F10",
        "N3",
        "F7",
        "R90",
        "F11"])
move_2(input_file)

# 30 mins parte 2
