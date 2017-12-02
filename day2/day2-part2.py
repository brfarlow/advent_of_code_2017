import itertools

with open('input.txt') as f:

    sum = 0

    for line in f:
        numbers = [int(i) for i in line.split()]
        for i,j in itertools.combinations(numbers,2):
            if i % j == 0:
                sum += i//j
            elif j % i == 0:
                sum += j//i

    print(sum)