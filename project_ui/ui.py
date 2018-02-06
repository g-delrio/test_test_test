import pygame
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys


class UI(QWidget):

    def __init__(self, total_size=450):
        super().__init__()
        self.left = 50
        self.right = 50
        self.board_size = int(total_size)
        self.square_size = self.board_size / 9
        self.title = 'Sample window'

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.board_size, self.board_size)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = UI(600)
    sys.exit(app.exec_())
