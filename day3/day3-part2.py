import sys


class Spiral:
    def __init__(self, puzzle_input):
        self.x = 0
        self.y = 0
        self.matrix = {(0, 0): 1, }
        self.puzzle_input = puzzle_input

    def check(self):
        value = 0
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if (i, j) in self.matrix:
                    value += self.matrix[(i, j)]
        self.matrix[(self.x, self.y)] = value

    def move_left(self):
        self.x -= 1
        self.check()

    def move_right(self):
        self.x += 1
        self.check()

    def move_up(self):
        self.y += 1
        self.check()

    def move_down(self):
        self.y -= 1
        self.check()

    def move(self):
        if abs(self.x) == abs(self.y):
            if self.x > 0 and self.y > 0:
                self.move_left()
            elif self.x < 0 and self.y > 0:
                self.move_down()
            elif (self.x <= 0 and self.y <= 0) or (self.x > 0 and self.y < 0):
                self.move_right()
        elif (self.x > 0) and (abs(self.y) < abs(self.x)):
            self.move_up()
        elif (self.y > 0) and (abs(self.x) < abs(self.y)):
            self.move_left()
        elif (self.x < 0) and (abs(self.y) < abs(self.x)):
            self.move_down()
        elif (self.y < 0) and (abs(self.x) < abs(self.y)):
            self.move_right()

    def goal(self):
        self.move()
        current = self.matrix[(self.x, self.y)]
        if self.matrix[(self.x, self.y)] < self.puzzle_input:
            return self.goal()
        else:
            return current


if __name__ == '__main__':

    spiral = Spiral(int(sys.argv[1]))
    print(spiral.goal())
