with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)


def find_seat_id(ins):
    row_1 = 0
    row_2 = 127
    col_1 = 0
    col_2 = 7

    for i in ins:
        if i == "B":
            row_1 = int((row_2-row_1)/2) + 1 + row_1
        if i == "F":
            row_2 = int((row_2-row_1)/2) + row_1
        if i == "R":
            col_1 = int((col_2-col_1)/2) + 1 + col_1
        if i == "L":
            col_2 = int((col_2-col_1)/2) + col_1
    return row_1*8 + col_1


max_id = 0
for i in input_file:
    max_id = max(max_id, find_seat_id(i))
print(max_id)

# 25 mins
seat_list = []
for i in input_file:
    seat_list += [find_seat_id(i)]
seat_list.sort()
print(seat_list)

prev = seat_list[0] - 1
for i in seat_list:
    if i - 1 != prev:
        print(i - 1)
        break
    prev = i

# 5 mins
