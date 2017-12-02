with open('input.txt') as f:

    sum = 0

    for line in f:
        numbers = [int(i) for i in line.split()]
        sum += max(numbers) - min(numbers)

    print(sum)