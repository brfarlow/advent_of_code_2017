with open('input.txt') as f:
    sum = 0
    file = f.readline()
    list = range(len(file))
    total = int(len(file))
    for index in list:
        new_index = index + (total/2)
        if file[list[index]] == file[list[int(new_index%total)]]:
                sum += int(file[list[index]])

    print(sum)