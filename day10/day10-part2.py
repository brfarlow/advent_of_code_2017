from functools import reduce
from operator import xor

lengths = [ord(x) for x in open('input.txt').read().rstrip()]
lengths.extend([17, 31, 73, 47, 23])
numbers = [x for x in range(256)]
cur_pos = 0
skip_size = 0
dense_hash = []

for i in range(64):
    for length in lengths:
        reverse = []

        for x in range(length):
            n = (cur_pos + x) % len(numbers)
            reverse.append(numbers[n])

        reverse.reverse()

        for x in range(length):
            n = (cur_pos + x) % len(numbers)
            numbers[n] = reverse[x]

        cur_pos += ((length + skip_size) % len(numbers))
        skip_size += 1


for i in range(16):
    portion = numbers[16 * i:16 * i + 16]
    dense_hash.append('%02x' % reduce(xor, portion))

print(''.join(dense_hash))
