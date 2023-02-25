def splitting(data):
    outer, inner = data.split("-")

    return int(outer), int(inner)

def number_in_number(data):
    count = 0

    for i in data:
        left, right = i.split(",")
        outer_left, inner_left = splitting(left)
        outer_right, inner_right = splitting(right)

        if outer_left >= outer_right and inner_left <= inner_right:
            count += 1
        elif outer_left <= outer_right and inner_left >= inner_right:
            count += 1

    return count

def overlap(data):
    count = 0

    for i in data:
        left, right = i.split(",")
        outer_left, inner_left = splitting(left)
        outer_right, inner_right = splitting(right)

        num_range = [i for i in range(outer_left, inner_left + 1)]

        for i in range(outer_right, inner_right + 1):
            if i in num_range:
                count += 1
                break

    return count



with open("day4.txt") as file_object:

    data = file_object.read()
    data_split = data.split("\n")
    data_split.remove('')

    print(number_in_number(data_split))
    print(overlap(data_split))
