import sys
import random

from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def run(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        for i in range(30):
            qp.setBrush(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)))
            d = random.randint(0, 100)
            qp.drawEllipse(random.randint(0, 755), random.randint(0, 574),
                           d, d)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())