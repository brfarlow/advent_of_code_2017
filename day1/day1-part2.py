with open('input.txt') as f:
    sum = 0
    file = f.read()
    file = list(map(int, file))
    length = len(file)

    sum = 0

    for index, val in enumerate(file):
        target = int(index + (length / 2))
        if val == file[target % length]:
            sum += val

    print(sum)
