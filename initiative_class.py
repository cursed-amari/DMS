# Form implementation generated from reading ui file 'alt_calc_init.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_init(object):
    windowClose = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 581, 421))
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.pushButton_add_enemy = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_add_enemy.setGeometry(QtCore.QRect(150, 400, 31, 23))
        self.pushButton_add_enemy.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/1/img/plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_add_enemy.setIcon(icon)
        self.pushButton_add_enemy.setObjectName("pushButton_add_enemy")
        self.pushButton_del_enemy = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_del_enemy.setGeometry(QtCore.QRect(190, 400, 31, 23))
        self.pushButton_del_enemy.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/1/img/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_del_enemy.setIcon(icon1)
        self.pushButton_del_enemy.setObjectName("pushButton_del_enemy")
        self.pushButton_redaction_enemy = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_redaction_enemy.setGeometry(QtCore.QRect(370, 400, 31, 23))
        self.pushButton_redaction_enemy.setText("")
        self.pushButton_redaction_enemy.setObjectName("pushButton_redaction_enemy")
        self.listWidget_initiative = QtWidgets.QListWidget(self.main_frame)
        self.listWidget_initiative.setGeometry(QtCore.QRect(150, 30, 256, 371))
        self.listWidget_initiative.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.listWidget_initiative.setObjectName("listWidget_initiative")
        self.pushButton_roll_initiative = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_roll_initiative.setGeometry(QtCore.QRect(230, 400, 31, 23))
        self.pushButton_roll_initiative.setText("")
        self.pushButton_roll_initiative.setObjectName("pushButton_roll_initiative")
        self.preset_frame = QtWidgets.QFrame(self.main_frame)
        self.preset_frame.setGeometry(QtCore.QRect(409, 30, 171, 371))
        self.preset_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.preset_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.preset_frame.setObjectName("preset_frame")
        self.listWidget_preset = QtWidgets.QListWidget(self.preset_frame)
        self.listWidget_preset.setGeometry(QtCore.QRect(0, 0, 171, 331))
        self.listWidget_preset.setObjectName("listWidget_preset")
        self.pushButton_del_preset = QtWidgets.QPushButton(self.preset_frame)
        self.pushButton_del_preset.setGeometry(QtCore.QRect(140, 340, 31, 23))
        self.pushButton_del_preset.setText("")
        self.pushButton_del_preset.setIcon(icon1)
        self.pushButton_del_preset.setObjectName("pushButton_del_preset")
        self.pushButton_add_preset = QtWidgets.QPushButton(self.preset_frame)
        self.pushButton_add_preset.setGeometry(QtCore.QRect(0, 340, 31, 23))
        self.pushButton_add_preset.setText("")
        self.pushButton_add_preset.setIcon(icon)
        self.pushButton_add_preset.setObjectName("pushButton_add_preset")
        self.pushButton_load_preset = QtWidgets.QPushButton(self.preset_frame)
        self.pushButton_load_preset.setGeometry(QtCore.QRect(40, 340, 31, 23))
        self.pushButton_load_preset.setText("")
        self.pushButton_load_preset.setObjectName("pushButton_load_preset")
        self.options_frame = QtWidgets.QFrame(self.main_frame)
        self.options_frame.setGeometry(QtCore.QRect(-1, 30, 151, 371))
        self.options_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.options_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.options_frame.setObjectName("options_frame")
        self.pushButton_apply_player_dice = QtWidgets.QPushButton(self.options_frame)
        self.pushButton_apply_player_dice.setGeometry(QtCore.QRect(40, 340, 93, 28))
        self.pushButton_apply_player_dice.setObjectName("pushButton_apply_player_dice")
        self.set_player_dice_edit_char_2 = QtWidgets.QLineEdit(self.options_frame)
        self.set_player_dice_edit_char_2.setGeometry(QtCore.QRect(90, 280, 51, 25))
        self.set_player_dice_edit_char_2.setObjectName("set_player_dice_edit_char_2")
        self.set_player_dice_edit_char_1 = QtWidgets.QLineEdit(self.options_frame)
        self.set_player_dice_edit_char_1.setGeometry(QtCore.QRect(90, 250, 51, 25))
        self.set_player_dice_edit_char_1.setObjectName("set_player_dice_edit_char_1")
        self.label_set_player_dice_char_1 = QtWidgets.QLabel(self.options_frame)
        self.label_set_player_dice_char_1.setGeometry(QtCore.QRect(10, 250, 71, 25))
        self.label_set_player_dice_char_1.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_1.setObjectName("label_set_player_dice_char_1")
        self.set_player_dice_edit_char_3 = QtWidgets.QLineEdit(self.options_frame)
        self.set_player_dice_edit_char_3.setGeometry(QtCore.QRect(90, 310, 51, 25))
        self.set_player_dice_edit_char_3.setObjectName("set_player_dice_edit_char_3")
        self.set_player_dice_edit_char_0 = QtWidgets.QLineEdit(self.options_frame)
        self.set_player_dice_edit_char_0.setGeometry(QtCore.QRect(90, 220, 51, 25))
        self.set_player_dice_edit_char_0.setObjectName("set_player_dice_edit_char_0")
        self.label_set_player_dice_char_2 = QtWidgets.QLabel(self.options_frame)
        self.label_set_player_dice_char_2.setGeometry(QtCore.QRect(10, 280, 71, 25))
        self.label_set_player_dice_char_2.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_2.setObjectName("label_set_player_dice_char_2")
        self.label_set_player_dice_char_3 = QtWidgets.QLabel(self.options_frame)
        self.label_set_player_dice_char_3.setGeometry(QtCore.QRect(10, 310, 71, 25))
        self.label_set_player_dice_char_3.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_3.setObjectName("label_set_player_dice_char_3")
        self.label_set_player_dice_char_0 = QtWidgets.QLabel(self.options_frame)
        self.label_set_player_dice_char_0.setGeometry(QtCore.QRect(10, 220, 71, 25))
        self.label_set_player_dice_char_0.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_0.setObjectName("label_set_player_dice_char_0")
        self.frame_frame = QtWidgets.QFrame(self.main_frame)
        self.frame_frame.setGeometry(QtCore.QRect(0, 0, 581, 31))
        self.frame_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_frame.setObjectName("frame_frame")
        self.label = QtWidgets.QLabel(self.frame_frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        self.pushButton_hide = QtWidgets.QPushButton(self.frame_frame)
        self.pushButton_hide.setGeometry(QtCore.QRect(510, 0, 31, 23))
        self.pushButton_hide.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hide.setIcon(icon2)
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.pushButton_close = QtWidgets.QPushButton(self.frame_frame)
        self.pushButton_close.setGeometry(QtCore.QRect(540, 0, 31, 23))
        self.pushButton_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_close.setIcon(icon3)
        self.pushButton_close.setObjectName("pushButton_close")
        self.checkBox_left_menu = QtWidgets.QCheckBox(self.main_frame)
        self.checkBox_left_menu.setGeometry(QtCore.QRect(0, 400, 70, 17))
        self.checkBox_left_menu.setObjectName("checkBox_left_menu")
        self.checkBox_right_menu = QtWidgets.QCheckBox(self.main_frame)
        self.checkBox_right_menu.setGeometry(QtCore.QRect(520, 400, 51, 17))
        self.checkBox_right_menu.setObjectName("checkBox_right_menu")
        self.pushButton_clear_list = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_clear_list.setGeometry(QtCore.QRect(320, 400, 31, 23))
        self.pushButton_clear_list.setText("")
        self.pushButton_clear_list.setObjectName("pushButton_clear_list")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_apply_player_dice.setText(_translate("MainWindow", "Refresh"))
        self.label_set_player_dice_char_1.setText(_translate("MainWindow", "Character 2"))
        self.label_set_player_dice_char_2.setText(_translate("MainWindow", "Character 3"))
        self.label_set_player_dice_char_3.setText(_translate("MainWindow", "Character 4"))
        self.label_set_player_dice_char_0.setText(_translate("MainWindow", "Character 1"))
        self.label.setText(_translate("MainWindow", "DnD Master support initiative"))
        self.checkBox_left_menu.setText(_translate("MainWindow", "options"))
        self.checkBox_right_menu.setText(_translate("MainWindow", "preset"))

        self.app_func_initiative_class()
        self.hide_func()
        self.set_style()

    def app_func_initiative_class(self):
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_hide.clicked.connect(self.showMinimized)

    def hide_func(self):
        self.options_frame.hide()
        self.preset_frame.hide()

    def set_style(self):
        pass

    def closeEvent(self, event):
        self.windowClose.emit()
        event.accept()

    # windowClose = QtCore.pyqtSignal()
    # self.pushButton_close.clicked.connect(MainWindow.close)
    # self.pushButton_hide.clicked.connect(MainWindow.showMinimized)
