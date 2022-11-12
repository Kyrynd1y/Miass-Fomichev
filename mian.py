import sys
import random

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from Ui import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.yellow = False
        self.pushButton.clicked.connect(self.DrawYellowCircle)
        self.pushButton_2.clicked.connect(self.DrawYellowCircle)

    def DrawYellowCircle(self):
        self.do_paint = True
        self.yellow = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            if self.yellow:
                color = QColor('yellow')
            else:
                color = QColor(random.randint(0, 0xffffff))
            qp.setBrush(color)
            r = random.randint(20, 100)
            w = self.width()
            h = self.height()
            qp.drawEllipse(QPoint(random.randint(r, w - r), random.randint(r, h - r)), r, r)
            qp.end()
            self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
