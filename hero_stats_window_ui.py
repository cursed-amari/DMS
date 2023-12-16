# Form implementation generated from reading ui file '.\hero_stats_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class HeroStatsUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame {\n"
"    background-color: rgb(85, 85, 85);\n"
"    opacity: 0.3;\n"
"    color: rgb(247, 147, 30);\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(55, 55, 55);\n"
"    color: rgb(247, 147, 30);\n"
"    border: none;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: rgb(55, 55, 55);\n"
"    color: rgb(247, 147, 30);\n"
"    border: none;\n"
"}\n"
"\n"
"QHBoxLayout {\n"
"    background-color: rgb(85, 85, 85);\n"
"    opacity: 0.3;\n"
"    color: rgb(247, 147, 30);\n"
"    border: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_ac = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ac.setObjectName("lineEdit_ac")
        self.horizontalLayout_2.addWidget(self.lineEdit_ac)
        self.lineEdit_speed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_speed.setObjectName("lineEdit_speed")
        self.horizontalLayout_2.addWidget(self.lineEdit_speed)
        self.lineEdit_hp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_hp.setObjectName("lineEdit_hp")
        self.horizontalLayout_2.addWidget(self.lineEdit_hp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_initiative = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initiative.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_initiative.setObjectName("lineEdit_initiative")
        self.verticalLayout.addWidget(self.lineEdit_initiative)
        self.label_str = QtWidgets.QLabel(self.centralwidget)
        self.label_str.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_str.setObjectName("label_str")
        self.verticalLayout.addWidget(self.label_str)
        self.label_dex = QtWidgets.QLabel(self.centralwidget)
        self.label_dex.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_dex.setObjectName("label_dex")
        self.verticalLayout.addWidget(self.label_dex)
        self.label_con = QtWidgets.QLabel(self.centralwidget)
        self.label_con.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_con.setObjectName("label_con")
        self.verticalLayout.addWidget(self.label_con)
        self.label_int = QtWidgets.QLabel(self.centralwidget)
        self.label_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_int.setObjectName("label_int")
        self.verticalLayout.addWidget(self.label_int)
        self.label_wis = QtWidgets.QLabel(self.centralwidget)
        self.label_wis.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_wis.setObjectName("label_wis")
        self.verticalLayout.addWidget(self.label_wis)
        self.label_cha = QtWidgets.QLabel(self.centralwidget)
        self.label_cha.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cha.setObjectName("label_cha")
        self.verticalLayout.addWidget(self.label_cha)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name.setText(_translate("MainWindow", "Name Race-Class Level"))
        self.lineEdit_ac.setText(_translate("MainWindow", "Ac"))
        self.lineEdit_speed.setText(_translate("MainWindow", "Speed"))
        self.lineEdit_hp.setText(_translate("MainWindow", "Hp"))
        self.lineEdit_initiative.setText(_translate("MainWindow", "Initiative"))
        self.label_str.setText(_translate("MainWindow", "Str"))
        self.label_dex.setText(_translate("MainWindow", "Dex"))
        self.label_con.setText(_translate("MainWindow", "Con"))
        self.label_int.setText(_translate("MainWindow", "Int"))
        self.label_wis.setText(_translate("MainWindow", "Wis"))
        self.label_cha.setText(_translate("MainWindow", "Cha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HeroStatsUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
