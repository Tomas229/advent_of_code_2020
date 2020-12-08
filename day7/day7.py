with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)


class Node:
    def __init__(self, name):
        self.name = name
        self.sons = []
        self.parents = []

    def add_parent(self, p):
        self.parents += [p]

    def add_son(self, s, n):
        self.sons += [[s, n]]

    def count_sons(self):
        count = 0
        for i in self.sons:
            count += int(i[1]) * i[0].count_sons()
        return count + 1

    def return_parents(self):
        parents_list = []
        for i in self.parents:
            parents_list += i.return_parents()
        parents_list += self.parents
        return parents_list

    def count_parents(self):
        return len(dict.fromkeys(self.return_parents()))  # De la perra


bags = []

for i in input_file:
    n = i.split("contain")

    p = n[0].replace(" bags", "")[:-1]
    pi = None
    for i in bags:
        if(p == i.name):
            pi = i
            break
    if(pi == None):
        pi = Node(p)
        bags += [pi]

    for i in n[1].split(","):
        if (i == " no other bags."):
            continue
        s = i.replace(".", "").replace("bags", "").replace(
            "bag", "")[3:-1]  # A LA MALA
        si = None
        for j in bags:
            if(s == j.name):
                si = j
                break
        if(si == None):
            si = Node(s)
            bags += [si]

        pi.add_son(si, i[1])
        si.add_parent(pi)


gold = None
for i in bags:
    if i.name == "shiny gold":
        gold = i
print(gold.count_parents())
# 2 horas  265
print(gold.count_sons() - 1)

# 10 mins 14177
