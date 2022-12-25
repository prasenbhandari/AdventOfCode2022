with open("day1.txt") as file_object:
    data = file_object.read()
    splt = data.split("\n\n")
    # print(splt[0])
    top_1, top_2, top_3 = 0, 0, 0

    top = []

    for x in splt:
        split_element = x.split("\n")
        # print(split_element[0])
        total = 0

        for i in range(0, len(split_element)):
            total = total + int(split_element[i])

        top.append(total)

        if total > top_1:
            top_1 = total
        if top_2 < total < top_1:
            top_2 = total
        if top_3 < total < top_2:
            top_3 = total

print(top_1)
print(top_2)
print(top_3)

total_2 = top_1 + top_2 + top_3

print(total_2)

top.sort()

print(top)
