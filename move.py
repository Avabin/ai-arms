from random import randint


class Move(object):
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance

    def __str__(self):
        return "Angle: " + str(self.angle) + ", Distance: " + str(self.distance)


def generate_moves(amount, range_of_drone):
    retval = list()
    for i in range(0, amount):
        angle = randint(0, 360)
        distance = randint(range_of_drone/4, range_of_drone)
        move = Move(angle, distance)
        retval.append(move)
    return retval