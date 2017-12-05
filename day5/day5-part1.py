with open('input.txt') as f:
    lines = f.readlines()
    lines = [int(x) for x in (line.strip("\n") for line in lines)]

    i = 0
    moves = 0
    while 0 <= i < len(lines):
        moves += 1
        lines[i] += 1
        i += lines[i] - 1

    print(moves)
