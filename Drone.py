from math import cos, sin, radians


class Drone(object):
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
        retval = "Drone:\n" + \
                 "Current Angle: " + str(self.current_angle) + "\n" \
                                                               "Position: " + str(self.pos) + "\n"
        for move, i in zip(self.moves, range(0, len(self.moves))):
            retval += "Move " + str(i) + ": " + str(move) + "\n"

        return retval


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)
