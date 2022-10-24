from PyQt6 import QtCore, QtGui, QtWidgets


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_init(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(309, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_calk_enemy = QtWidgets.QLabel(self.centralwidget)
        self.label_calk_enemy.setGeometry(QtCore.QRect(10, 10, 160, 331))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_calk_enemy.setFont(font)
        self.label_calk_enemy.setStyleSheet("font-weight:bold")
        self.label_calk_enemy.setText("")
        self.label_calk_enemy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calk_enemy.setObjectName("label_calk_enemy")
        self.pushButton_initiative = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_initiative.setGeometry(QtCore.QRect(30, 350, 120, 25))
        self.pushButton_initiative.setObjectName("pushButton_initiative")
        self.enemy_name = QtWidgets.QLabel(self.centralwidget)
        self.enemy_name.setGeometry(QtCore.QRect(180, 10, 120, 25))
        self.enemy_name.setStyleSheet("font-weight:bold")
        self.enemy_name.setObjectName("enemy_name")
        self.enemy_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.enemy_name_edit.setGeometry(QtCore.QRect(180, 40, 120, 25))
        self.enemy_name_edit.setObjectName("enemy_name_edit")
        self.enemy_initiative = QtWidgets.QLabel(self.centralwidget)
        self.enemy_initiative.setGeometry(QtCore.QRect(180, 80, 120, 25))
        self.enemy_initiative.setStyleSheet("font-weight:bold")
        self.enemy_initiative.setObjectName("enemy_initiative")
        self.enemy_initiative_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.enemy_initiative_edit.setGeometry(QtCore.QRect(180, 110, 120, 25))
        self.enemy_initiative_edit.setObjectName("enemy_initiative_edit")
        self.label_enemy = QtWidgets.QLabel(self.centralwidget)
        self.label_enemy.setGeometry(QtCore.QRect(180, 180, 121, 191))
        self.label_enemy.setText("")
        self.label_enemy.setObjectName("label_enemy")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(220, 140, 41, 28))
        self.pushButton_add.setObjectName("pushButton")
        self.pushButton_clean_enemy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clean_enemy.setGeometry(QtCore.QRect(180, 390, 120, 25))
        self.pushButton_clean_enemy.setObjectName("pushButton_clean_enemy")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculating initiative"))
        self.pushButton_initiative.setText(_translate("MainWindow", "Initiative"))
        self.enemy_name.setText(_translate("MainWindow", "Name"))
        self.enemy_initiative.setText(_translate("MainWindow", "Initiative"))
        self.pushButton_add.setText(_translate("MainWindow", "add"))
        self.pushButton_clean_enemy.setText(_translate("MainWindow", "Clear"))