# Form implementation generated from reading ui file 'redaction_hp_tracker.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_redaction_hp_tracker(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(125, 128)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(85, 85, 85);\n"
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
        self.label_current_hp = QtWidgets.QLabel(self.frame)
        self.label_current_hp.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.label_current_hp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_current_hp.setObjectName("label_current_hp")
        self.label_current_hp.setStyleSheet("font-weight: bold;")
        self.label_view_current_hp = QtWidgets.QLabel(self.frame)
        self.label_view_current_hp.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_view_current_hp.setObjectName("label_view_current_hp")
        self.edit_new_hp = QtWidgets.QLineEdit(self.frame)
        self.edit_new_hp.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.edit_new_hp.setObjectName("edit_new_hp")
        self.pushButton_add_hp = QtWidgets.QPushButton(self.frame)
        self.pushButton_add_hp.setGeometry(QtCore.QRect(10, 100, 31, 23))
        self.pushButton_add_hp.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon/plus.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_add_hp.setIcon(icon)
        self.pushButton_add_hp.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_add_hp.setObjectName("pushButton_add_hp")
        self.pushButton_minus_hp = QtWidgets.QPushButton(self.frame)
        self.pushButton_minus_hp.setGeometry(QtCore.QRect(50, 100, 31, 23))
        self.pushButton_minus_hp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icon/minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_minus_hp.setIcon(icon1)
        self.pushButton_minus_hp.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_minus_hp.setObjectName("pushButton_minus_hp")
        self.pushButton_set_hp = QtWidgets.QPushButton(self.frame)
        self.pushButton_set_hp.setGeometry(QtCore.QRect(90, 10, 31, 23))
        self.pushButton_set_hp.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_set_hp.setObjectName("pushButton_set_hp")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(90, 100, 31, 23))
        self.pushButton_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icon/x.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_restore_hp = QtWidgets.QPushButton(self.frame)
        self.pushButton_restore_hp.setGeometry(QtCore.QRect(90, 40, 31, 23))
        self.pushButton_restore_hp.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/icon/restore.ico"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton_restore_hp.setIcon(icon3)
        self.pushButton_restore_hp.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_restore_hp.setObjectName("pushButton_restore_hp")
        self.horizontalLayout.addWidget(self.frame)

        self.pushButton_add_hp.clicked.connect(Dialog.close)
        self.pushButton_minus_hp.clicked.connect(Dialog.close)
        self.pushButton_set_hp.clicked.connect(Dialog.close)
        self.pushButton_restore_hp.clicked.connect(Dialog.close)
        self.pushButton_close.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_current_hp.setText(_translate("Dialog", "Current HP"))
        self.label_view_current_hp.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_set_hp.setText(_translate("Dialog", "Set"))
