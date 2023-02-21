def find_value(common_letter):

    if "z" >= common_letter >= "a":
        value = ord(common_letter) - 96
    else:
        value = ord(common_letter) - 38

    return value


def grouping(data):

    main = []
    sub = []
    count = 0

    for i in data:
        sub.append(i)
        count += 1

        if count % 3 == 0:
            main.append(sub[:])
            sub.clear()

    return main


with open("day3.txt") as file_object:
    sum = 0

    data = file_object.read()
    splt = data.split("\n")
    splt.remove('')

    #part 1
    """split1 = ''
    split2 = ''

    for x in splt:
        split1 = x[:len(x) // 2]
        split2 = x[len(x) // 2:]

        for i in split1:
            if i in split2:
                sum += find_value(i)
                break

    print(sum)"""

    #part 2

    group_of_3 = grouping(splt)

    for x in group_of_3:
        for i in x[0]:
            if i in x[1] and i in x[2]:
                sum += find_value(i)
                break

    print(sum)
