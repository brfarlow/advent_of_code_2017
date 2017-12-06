import numpy as np

input = open('input.txt').read().split()
input = [int(x) for x in input]

count = 0
seen = {}

while tuple(input) not in seen:
    seen[tuple(input)] = count
    count += 1

    index = np.argmax(input)
    value = input[index]
    input[index] = 0

    while value > 0:
        index += 1
        index %= len(input)
        input[index] += 1
        value -= 1


print(count - seen[tuple(input)])
