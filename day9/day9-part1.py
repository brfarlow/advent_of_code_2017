input = open('input.txt').read()
score = 0
depth = 0
in_garbage = False
skip = False

for char in input:
    if in_garbage:
        if skip:
            skip = False
        elif char == "!":
            skip = True
        elif char == ">":
            in_garbage = False
    else:
        if char == "{":
            depth += 1
        elif char == "}":
            score += depth
            depth -= 1
        elif char == "<":
            in_garbage = True

print(score)
