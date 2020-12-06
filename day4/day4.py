import re
with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)

    credential_lists = [""]
    index = 0
    for i in input_file:
        if(i == ""):
            index += 1
            credential_lists += [""]

        credential_lists[index] = credential_lists[index] + i + " "
    for i in range(len(credential_lists)):
        credential_lists[i] = credential_lists[i].split()

    dict_list = []
    for l in credential_lists:
        new_dict = dict()
        for i in l:
            aux = i.split(":")
            new_dict[aux[0]] = aux[1]
        dict_list += [new_dict]

    def count_present(dict_list):
        count = 0
        for d in dict_list:

            if((d.get("byr") and d.get("iyr") and d.get("eyr") and d.get("hgt") and d.get("hcl") and d.get("ecl") and d.get("pid")) != None):
                count += 1
        return count
    # 45 mins
    print(count_present(dict_list))

    def count_valid(dict_list):
        count = 0
        for d in dict_list:
            if((d.get("byr") and d.get("iyr") and d.get("eyr") and d.get("hgt") and d.get("hcl") and d.get("ecl") and d.get("pid")) == None):
                continue
            if(1920 > int(d.get("byr")) or int(d.get("byr")) > 2002):
                continue
            if(2010 > int(d.get("iyr")) or int(d.get("iyr")) > 2020):
                continue
            if(2020 > int(d.get("eyr")) or int(d.get("eyr")) > 2030):
                continue
            if(d.get("hgt")[-2:] != "cm" and d.get("hgt")[-2:] != "in"):
                continue
            if(d.get("hgt")[-2:] == "cm" and (150 > int(d.get("hgt")[:-2]) or int(d.get("hgt")[:-2]) > 193)):
                continue
            if(d.get("hgt")[-2:] == "in" and (59 > int(d.get("hgt")[:-2]) or int(d.get("hgt")[:-2]) > 76)):
                continue
            if(d.get("hcl")[0] != "#"):
                continue
            if(len(d.get("hcl")) != 7):
                continue
            if(re.match("[0-9a-fA-F]+", d.get("hcl")[1:]) == None):
                continue
            if d.get("ecl") not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            if (len(d.get("pid")) != 9):
                continue
            if (re.match("\d", d.get("pid")) == None):
                continue
            count += 1
        return count
print(count_valid(dict_list))

# 1hr  aprox
