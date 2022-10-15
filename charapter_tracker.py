import random
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('My App')
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Базовый текст')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.button = QtWidgets.QPushButton(self)
        self.button.move(70, 150)
        self.button.setText('Кнопка')
        self.button.setFixedWidth(200)
        self.button.clicked.connect(self.add_lable)


    def add_lable(self):
        self.new_text.setText('Add')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()
