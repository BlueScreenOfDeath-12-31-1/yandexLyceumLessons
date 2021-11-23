import sys
import random

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
import PyQt5.uic


class MyWindow(QWidget):
    def paint(self):
        self.do_paint = True
        self.repaint()

    def __init__(self):
        super().__init__()
        # self.initUI()
        PyQt5.uic.loadUi("UI.ui", self)
        self.do_paint = False

        # def t(s):
        #     s.do_paint = True

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            # self.draw_flag(qp)
            qp.setPen(QColor(125, 175, 200))
            qp.setBrush(QColor(230, 230, 100))
            r = random.randint(50, 200) * 1.0
            qp.drawEllipse(QRectF(100.0, 100.0, r, r))
            # Завершаем рисование
            qp.end()
            self.do_paint = False
        # print("qq")
        return super().paintEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
