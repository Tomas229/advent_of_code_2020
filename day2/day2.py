def pass_word(l):
    max_count = 0
    for i in l:
        aux = i.split()
        letter = aux[1][0]  # str
        count = 0

        for j in aux[2]:
            if j == letter:
                count += 1

        low_num = int(aux[0].split("-")[0])
        high_num = int(aux[0].split("-")[1])

        if (low_num <= count and count <= high_num):
            max_count += 1
    return max_count


with open("password.txt") as file:
    pass_file = file.readlines()
    for i in range(len(pass_file)):
        pass_file[i] = pass_file[i][0:-1]

    print(pass_word(pass_file))

# 37 mins


# Part II
def pass_word_2(l):
    max_count = 0
    for i in l:
        aux = i.split()
        letter = aux[1][0]  # str

        low_num = int(aux[0].split("-")[0]) - 1
        high_num = int(aux[0].split("-")[1]) - 1

        if ((aux[2][low_num] == letter) ^ (aux[2][high_num] == letter)):
            max_count += 1
    return max_count


with open("password.txt") as file:
    pass_file = file.readlines()
    for i in range(len(pass_file)-1):
        pass_file[i] = pass_file[i][0:-1]

    print(pass_word_2(pass_file))
