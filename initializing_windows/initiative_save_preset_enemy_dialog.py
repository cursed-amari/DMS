# Form implementation generated from reading ui file 'initiative_new.save_preset_enemy_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_save_preset_enemy(object):
    def setupUi(self, Dialog_save_preset_enemy):
        Dialog_save_preset_enemy.setObjectName("Dialog_save_preset_enemy")
        Dialog_save_preset_enemy.resize(121, 91)
        self.frame = QtWidgets.QFrame(Dialog_save_preset_enemy)
        self.frame.setGeometry(QtCore.QRect(0, 0, 121, 91))
        self.frame.setStyleSheet("QFrame {\n"
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
"QPushButton {\n"
"    background: rgb(55, 55, 55);\n"
"    border-radius: 5px;\n"
"    color: rgb(247, 147, 30);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(105, 105, 105);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.preset_name_edit = QtWidgets.QLineEdit(self.frame)
        self.preset_name_edit.setGeometry(QtCore.QRect(0, 30, 120, 25))
        self.preset_name_edit.setObjectName("preset_name_edit")
        self.enemy_name = QtWidgets.QLabel(self.frame)
        self.enemy_name.setGeometry(QtCore.QRect(0, 0, 120, 25))
        self.enemy_name.setStyleSheet("font-weight:bold")
        self.enemy_name.setObjectName("enemy_name")
        self.pushButton_cansel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cansel.setGeometry(QtCore.QRect(70, 60, 31, 23))
        self.pushButton_cansel.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon/x.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cansel.setIcon(icon)
        self.pushButton_cansel.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_cansel.setObjectName("pushButton_cansel")
        self.pushButton_ok = QtWidgets.QPushButton(self.frame)
        self.pushButton_ok.setGeometry(QtCore.QRect(10, 60, 31, 23))
        self.pushButton_ok.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icon/plus.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_ok.setIcon(icon1)
        self.pushButton_ok.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.pushButton_ok.clicked.connect(Dialog_save_preset_enemy.close)
        self.pushButton_cansel.clicked.connect(Dialog_save_preset_enemy.close)

        self.retranslateUi(Dialog_save_preset_enemy)
        QtCore.QMetaObject.connectSlotsByName(Dialog_save_preset_enemy)

    def retranslateUi(self, Dialog_save_preset_enemy):
        _translate = QtCore.QCoreApplication.translate
        Dialog_save_preset_enemy.setWindowTitle(_translate("Dialog_save_preset_enemy", "Dialog"))
        self.enemy_name.setText(_translate("Dialog_save_preset_enemy", "Preset name"))