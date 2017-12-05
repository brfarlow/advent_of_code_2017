with open('input.txt') as f:
    file = f.read()
    file = list(map(int, file))
    length = len(file)

    sum = 0

    for index, val in enumerate(file):
        target = index + 1
        if val == file[target % length]:
            sum += val

    print(sum)
