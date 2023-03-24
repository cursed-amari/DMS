# Form implementation generated from reading ui file 'initiative_new.redaction_enemy_dialog_2.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_redaction_enemy_in_initiative(object):
    def setupUi(self, Dialog_redaction_enemy_in_initiative):
        Dialog_redaction_enemy_in_initiative.setObjectName("Dialog_redaction_enemy_in_initiative")
        Dialog_redaction_enemy_in_initiative.resize(94, 121)
        self.frame = QtWidgets.QFrame(Dialog_redaction_enemy_in_initiative)
        self.frame.setGeometry(QtCore.QRect(0, 0, 121, 121))
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
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.enemy_hp = QtWidgets.QLabel(self.frame)
        self.enemy_hp.setGeometry(QtCore.QRect(10, 0, 21, 25))
        self.enemy_hp.setStyleSheet("font-weight:bold")
        self.enemy_hp.setObjectName("enemy_hp")
        self.enemy_hp_edit = QtWidgets.QLineEdit(self.frame)
        self.enemy_hp_edit.setGeometry(QtCore.QRect(10, 30, 71, 25))
        self.enemy_hp_edit.setObjectName("enemy_hp_edit")
        self.pushButton_cansel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cansel.setGeometry(QtCore.QRect(50, 90, 31, 23))
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
        self.enemy_current_hp = QtWidgets.QLabel(self.frame)
        self.enemy_current_hp.setGeometry(QtCore.QRect(40, 0, 41, 25))
        self.enemy_current_hp.setStyleSheet("font-weight:bold")
        self.enemy_current_hp.setObjectName("enemy_current_hp")
        self.pushButton_minus_hp = QtWidgets.QPushButton(self.frame)
        self.pushButton_minus_hp.setGeometry(QtCore.QRect(50, 60, 31, 23))
        self.pushButton_minus_hp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icon/minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_minus_hp.setIcon(icon2)
        self.pushButton_minus_hp.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_minus_hp.setObjectName("pushButton_minus_hp")
        self.pushButton_set_hp = QtWidgets.QPushButton(self.frame)
        self.pushButton_set_hp.setGeometry(QtCore.QRect(10, 90, 31, 23))
        self.pushButton_set_hp.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_set_hp.setObjectName("pushButton_set_hp")

        self.pushButton_ok.clicked.connect(Dialog_redaction_enemy_in_initiative.close)
        self.pushButton_cansel.clicked.connect(Dialog_redaction_enemy_in_initiative.close)
        self.pushButton_minus_hp.clicked.connect(Dialog_redaction_enemy_in_initiative.close)
        self.pushButton_set_hp.clicked.connect(Dialog_redaction_enemy_in_initiative.close)

        self.retranslateUi(Dialog_redaction_enemy_in_initiative)
        QtCore.QMetaObject.connectSlotsByName(Dialog_redaction_enemy_in_initiative)

    def retranslateUi(self, Dialog_redaction_enemy_in_initiative):
        _translate = QtCore.QCoreApplication.translate
        Dialog_redaction_enemy_in_initiative.setWindowTitle(
            _translate("Dialog_redaction_enemy_in_initiative", "Dialog"))
        self.enemy_hp.setText(_translate("Dialog_redaction_enemy_in_initiative", "HP"))
        self.enemy_current_hp.setText(_translate("Dialog_redaction_enemy_in_initiative", "HP"))
        self.pushButton_set_hp.setText(_translate("Dialog_redaction_enemy_in_initiative", "Set"))