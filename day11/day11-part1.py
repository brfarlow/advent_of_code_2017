input = open('input.txt').read().split(',')

pos = (0, 0)
directions = {'n': (0, 1),
              's': (0, -1),
              'nw': (-1, 1),
              'ne': (1, 0),
              'sw': (-1, 0),
              'se': (1, -1)}

for direction in input:
    pos = (pos[0] + directions[direction][0],
           pos[1] + directions[direction][1])

print(max(abs(pos[0]), abs(pos[1]), abs(pos[0] + pos[1])))
