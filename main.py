from math import sin, cos, radians
from random import randint

from Drone import Position, Drone
from move import Move, generate_moves

x = Drone()
x.pos = Position(0, 0)
x.apply_moves([Move(90, 10), Move(0, 10), Move(180, 10), Move(270, 10), Move(45, 12)])

print(str(x))

mov = generate_moves(10, 10)
x.apply_moves(mov)

print(str(x))
