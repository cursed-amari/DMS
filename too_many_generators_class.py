# Form implementation generated from reading ui file 'too_many_generators.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_too_many_generators(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 581, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.comboBox_choose_generater = QtWidgets.QComboBox(self.frame)
        self.comboBox_choose_generater.setGeometry(QtCore.QRect(10, 10, 331, 20))
        self.comboBox_choose_generater.setObjectName("comboBox_choose_generater")
        self.pushButton_open_full_txt = QtWidgets.QPushButton(self.frame)
        self.pushButton_open_full_txt.setGeometry(QtCore.QRect(520, 10, 51, 23))
        self.pushButton_open_full_txt.setObjectName("pushButton_open_full_txt")
        self.textEdit_text_generator = QtWidgets.QTextEdit(self.frame)
        self.textEdit_text_generator.setGeometry(QtCore.QRect(10, 40, 561, 381))
        self.textEdit_text_generator.setObjectName("textEdit_text_generator")
        self.pushButton_random = QtWidgets.QPushButton(self.frame)
        self.pushButton_random.setGeometry(QtCore.QRect(450, 10, 51, 23))
        self.pushButton_random.setObjectName("pushButton_random")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_open_full_txt.setText(_translate("MainWindow", "Open all"))
        self.pushButton_random.setText(_translate("MainWindow", "Random"))
