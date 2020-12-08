from string import ascii_lowercase
with open("input.txt") as file:
    input_file = file.read()
    input_file = input_file.split('\n\n')

    for i in range(len(input_file)):
        input_file[i] = input_file[i].replace('\n', "")

# print(input_file)


def count_letter(input):
    list_l = [0]*26

    for i in input:
        list_l[ascii_lowercase.find(i)] = 1

    count = 0
    for i in list_l:
        count += i

    return count, list_l


max_count = 0
for i in input_file:
    x, y = count_letter(i)
    max_count += x

# print(max_count)
# 50 mins - 6457

with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)

    def presenc(l):
        presence_list = []
        for i in l:
            if i == "":
                presence_list += [""]
            else:
                x, y = count_letter(i)
                presence_list += [y]
        return presence_list

    # print(presence_list)

    def and_product(l1, l2):
        res = []
        for i in range(len(l1)):
            res += [l1[i] & l2[i]]
        return res

    def count_groups(p_list):
        new_list = []
        current = [1]*26

        for i in p_list:

            if(i == ""):
                new_list += [current]
                current = [1]*26
            else:
                current = and_product(current, i)

        new_list += [current]

        final_count = 0
        for l in new_list:
            for i in l:
                final_count += i

        return final_count

    print(count_groups(presenc(input_file)))

print(count_groups(presenc(["abc", "", "a", "b", "c",
                            "", "ab", "ac", "", "a", "a", "a", "a", "", "b"])))

# 1 h 10 m
