lengths = [int(x) for x in open('input.txt').read().split(',')]
numbers = [x for x in range(256)]
cur_pos = 0
skip_size = 0

for length in lengths:
    reverse = []

    for x in range(length):
        n = (cur_pos + x) % 256
        reverse.append(numbers[n])

    reverse.reverse()

    for x in range(length):
        n = (cur_pos + x) % 256
        numbers[n] = reverse[x]

    cur_pos += ((length + skip_size) % 256)
    skip_size += 1

print(numbers[0] * numbers[1])
