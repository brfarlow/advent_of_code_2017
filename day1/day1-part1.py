with open('input.txt') as f:
    sum = 0
    file = f.readline()
    list = range(len(file))
    for index in list[:-1]:
        if(file[index] == file[index+1]):
            sum += int(file[index])
    if file[list[-1]] == file[list[0]]:
        sum += int(file[list[0]])

    print(sum)