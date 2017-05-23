from PyQt5.QtWidgets import QWidget


class GUI(QWidget):
    def __init__(self):
        super().__init__()

    def init_gui(self):
        self.setGeometry(300, 300, 480, 320)
        self.setWindowTitle("Hello!")
        self.show()
