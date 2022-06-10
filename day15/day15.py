input = [0, 5, 4, 1, 10, 14, 7]


def game(l):
    index = len(l)-1
    keys = dict()
    for j in l:
        keys[j] = l.index(j)

    while index < 2020-1:
        num_i = l.index(l[index])
        if index == num_i:
            l += [0]
            keys[l[index]] = index
        else:
            l += [index - keys[l[index]]]
            keys[l[index]] = index
        index += 1
    return l[index]


print(game([0, 3, 6]))
print(game(input))

# parte 1  37 min
