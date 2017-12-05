with open('input.txt') as f:
    valid_passphrases = 0

    for line in f.readlines():
        phrases = [('').join(sorted(x)) for x in line.split()]
        if len(phrases) == len(set(phrases)):
            valid_passphrases += 1

    print(valid_passphrases)
