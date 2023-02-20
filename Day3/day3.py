def find_value(common_letter):

    if "z" >= common_letter >= "a":
        value = ord(common_letter) - 96
    else:
        value = ord(common_letter) - 38

    return value


with open("day3.txt") as file_object:
    sum = 0

    data = file_object.read()
    splt = data.split("\n")
    splt.remove('')

    split1 = ''
    split2 = ''

    #part 1
    for x in splt:
        split1 = x[:len(x) // 2]
        split2 = x[len(x) // 2:]

        for i in split1:
            if i in split2:
                sum += find_value(i)
                break

    print(sum)

    #part 2
    for x in splt:
        group = x
