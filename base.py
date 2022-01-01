import math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def add_label():
    print('test')

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Quadratic equation')
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText('База')
    main_text.move(150, 50)
    main_text.adjustSize()

    button = QtWidgets.QPushButton(window)
    button.move(75, 100)
    button.setText('Базована кнопка')
    button.setFixedWidth(200)
    button.clicked.connect(add_label)
    window.show()
    sys.exit(app.exec_())


application()
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
D = math.pow(b, 2) - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print('x1=', round(x1, 3))
    print('x2=', round(x2, 3))
elif D == 0:
    x = -b / 2 * a
    print('x=', round(x, 3))
else:
    d = D * -1

    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
    x1 = complex(0, x1)
    x2 = complex(0, x2)

    print('x1=', x1)
    print('x2=', x2)
