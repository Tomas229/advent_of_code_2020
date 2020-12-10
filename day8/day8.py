with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)


def assembler(l):
    visited = []
    for i in l:
        visited += [[i, 0]]
    index = 0
    prev_index = -1
    acc = 0

    while (visited[index][1] != 1):
        visited[index][1] = 1
        aux = visited[index][0].split(" ")
        if(aux[0] == "nop"):
            prev_index = index
            index += 1

        if(aux[0] == "jmp"):
            prev_index = index
            index += int(aux[1])

        if(aux[0] == "acc"):
            acc += int(aux[1])
            prev_index = index
            index += 1

    return acc, prev_index


print(assembler(input_file))

# 25 mins parte 1 1586


def assembler_fixer(l):
    index = 0
    acc = 0

    x, y = assembler(input_file)

    while index < len(l):
        aux = l[index].split(" ")

        if index == y:
            if(aux[0] == "nop"):
                aux[0] = "jmp"

            elif (aux[0] == "jmp"):
                aux[0] = "nop"

        if(aux[0] == "nop"):
            index += 1

        if(aux[0] == "jmp"):
            index += int(aux[1])

        if(aux[0] == "acc"):
            acc += int(aux[1])
            index += 1

    return acc


print(assembler_fixer(input_file))
# 25 mins aún no lo logro
