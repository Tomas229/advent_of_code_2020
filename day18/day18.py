with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
        input_file[i] = [char for char in list(input_file[i].replace(" ", ""))]
    # print(input_file)


def aux(l):
    i = 0
    new_list = []
    while i < len(l):
        if l[i] == "(":
            j = i + 1
            h = 0
            while l[j] != ")" or h > 0:
                if l[j] == "(":
                    h += 1
                if l[j] == ")":
                    h -= 1
                j += 1
            new_list += [solve(l[i+1:j])]
            i = j
        else:
            new_list += [l[i]]
        i += 1
    return new_list


def solve(l):
    new_list = aux(l)
    count = int(new_list[0])
    new_list = new_list[1:]
    index = 0
    while(index < len(new_list)):
        if new_list[index] == "+":
            count += int(new_list[index + 1])
        elif new_list[index] == "*":
            count *= int(new_list[index + 1])
        index += 2
    return count


def final(l):
    count = 0
    for i in l:
        count += solve(i)
    return count


#print(solve(["2", "*", "3", "+", "(", "4", "*", "5", ")"]))
print(final(input_file))

# primera parte 1 hora 30 mins
