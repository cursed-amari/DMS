# Form implementation generated from reading ui file '.\img_viewer_new_token.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_new_token(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(130, 70)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
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
        self.edit_name = QtWidgets.QLineEdit(self.frame)
        self.edit_name.setGeometry(QtCore.QRect(10, 5, 111, 31))
        self.edit_name.setObjectName("edit_name")
        self.pushButton_accept = QtWidgets.QPushButton(self.frame)
        self.pushButton_accept.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.pushButton_accept.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_accept.setText(_translate("Dialog", "Accept"))
