from math import sin, cos, radians
from random import randint

import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget
from Drone import Position, Drone
from GUI import GUI
from move import Move, generate_moves


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = GUI()

    w.init_gui()

    sys.exit(app.exec_())
