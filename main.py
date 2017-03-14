from math import sin, cos, radians
from random import randint


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)


class Move(object):
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance

    def __str__(self):
        return "Angle: " + str(self.angle) + ", Distance: " + str(self.distance)


class Entity(object):
    def __init__(self):
        self.current_angle = 0
        self.moves = list()
        self.pos = Position(0, 0)

    def apply_move(self, move):
        self.moves.append(move)
        self.current_angle = move.angle
        self.pos.x += round(move.distance * cos(radians(move.angle)), 2)
        self.pos.y += round(move.distance * sin(radians(move.angle)), 2)
        print(str(self))

    def apply_moves(self, moves):
        for move in moves:
            self.apply_move(move)

    def __str__(self):
        retval = "Entity:\n" + \
                 "Current Angle: " + str(self.current_angle) + "\n" \
                                                               "Position: " + str(self.pos) + "\n"
        for move, i in zip(self.moves, range(0, len(self.moves))):
            retval += "Move " + str(i) + ": " + str(move) + "\n"

        return retval


def generate_moves(amount, range):
    retval = list()
    for i in range(0, amount):
        angle = randint(0, 360)
        distance = randint(0 - range, range)
        move = Move(angle, distance)
        retval.append(move)

    return retval

x = Entity()
x.pos = Position(0, 0)
x.apply_moves([Move(90, 10), Move(0, 10), Move(180, 10), Move(270, 10), Move(45, 12)])

print(str(x))

mov = generate_moves(10, 10)
x.apply_moves(mov)

print(str(x))
