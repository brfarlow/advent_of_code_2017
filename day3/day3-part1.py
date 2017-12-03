# Calculate the nearest odd perfect square n2 from your input
# and you have a number that is n-1 Manhattan distance away
# from the center (the bottom right corner).
# Then count the distance from your input.
puzzle_input = 277678
closest_square_root = int(puzzle_input ** 0.5)

if closest_square_root % 2 == 0:
    size = closest_square_root + 1
else:
    size = closest_square_root + 2

last_square = (size - 2) ** 2
difference = puzzle_input - last_square
minus = size - 1
corners_and_square = list()

for i in range(5):
    corners_and_square.append(last_square + i * minus)

half = size // 2

if puzzle_input == last_square:
    distance = size - 2
elif difference % (size - 1) == 0:
    distance = size - 1
else:
    for i in range(1, 5):
        if puzzle_input < corners_and_square[i]:
            dx = half
            dy = abs(
                ((size - 2) // 2) -
                (puzzle_input - corners_and_square[i - 1] - 1)
            )

            distance = dx + dy
            break
            
print(distance)
