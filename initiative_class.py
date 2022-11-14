from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_init(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 581, 461))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_delete_character = QtWidgets.QLabel(self.frame)
        self.label_delete_character.setGeometry(QtCore.QRect(10, 210, 120, 25))
        self.label_delete_character.setStyleSheet("font-weight:bold")
        self.label_delete_character.setObjectName("label_delete_character")
        self.load_preset_2 = QtWidgets.QLabel(self.frame)
        self.load_preset_2.setGeometry(QtCore.QRect(450, 360, 81, 25))
        self.load_preset_2.setStyleSheet("font-weight:bold")
        self.load_preset_2.setObjectName("load_preset_2")
        self.set_player_dice_edit_char_3 = QtWidgets.QLineEdit(self.frame)
        self.set_player_dice_edit_char_3.setGeometry(QtCore.QRect(100, 360, 51, 25))
        self.set_player_dice_edit_char_3.setObjectName("set_player_dice_edit_char_3")
        self.label_enemy_initiative_redaction = QtWidgets.QLabel(self.frame)
        self.label_enemy_initiative_redaction.setGeometry(QtCore.QRect(10, 110, 61, 25))
        self.label_enemy_initiative_redaction.setStyleSheet("font-weight:bold")
        self.label_enemy_initiative_redaction.setObjectName("label_enemy_initiative_redaction")
        self.label_set_player_dice_char_3 = QtWidgets.QLabel(self.frame)
        self.label_set_player_dice_char_3.setGeometry(QtCore.QRect(10, 360, 81, 25))
        self.label_set_player_dice_char_3.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_3.setObjectName("label_set_player_dice_char_3")
        self.label_enemy = QtWidgets.QLabel(self.frame)
        self.label_enemy.setGeometry(QtCore.QRect(450, 150, 121, 141))
        self.label_enemy.setText("")
        self.label_enemy.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_enemy.setObjectName("label_enemy")
        self.label_set_player_dice_char_0 = QtWidgets.QLabel(self.frame)
        self.label_set_player_dice_char_0.setGeometry(QtCore.QRect(10, 270, 81, 25))
        self.label_set_player_dice_char_0.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_0.setObjectName("label_set_player_dice_char_0")
        self.label_calk_enemy = QtWidgets.QLabel(self.frame)
        self.label_calk_enemy.setGeometry(QtCore.QRect(220, 10, 160, 371))
        self.label_calk_enemy.setStyleSheet("font-weight:bold")
        self.label_calk_enemy.setText("")
        self.label_calk_enemy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calk_enemy.setObjectName("label_calk_enemy")
        self.pushButton_apply_player_dice = QtWidgets.QPushButton(self.frame)
        self.pushButton_apply_player_dice.setGeometry(QtCore.QRect(40, 390, 93, 28))
        self.pushButton_apply_player_dice.setObjectName("pushButton_apply_player_dice")
        self.edit_name_redaction = QtWidgets.QLineEdit(self.frame)
        self.edit_name_redaction.setGeometry(QtCore.QRect(10, 70, 115, 25))
        self.edit_name_redaction.setObjectName("edit_name_redaction")
        self.box_select_character = QtWidgets.QComboBox(self.frame)
        self.box_select_character.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.box_select_character.setObjectName("box_select_character")
        self.enemy_initiative_edit = QtWidgets.QLineEdit(self.frame)
        self.enemy_initiative_edit.setGeometry(QtCore.QRect(450, 100, 61, 25))
        self.enemy_initiative_edit.setObjectName("enemy_initiative_edit")
        self.load_preset = QtWidgets.QPushButton(self.frame)
        self.load_preset.setGeometry(QtCore.QRect(530, 390, 41, 22))
        self.load_preset.setObjectName("load_preset")
        self.del_preset = QtWidgets.QPushButton(self.frame)
        self.del_preset.setGeometry(QtCore.QRect(540, 370, 31, 22))
        self.del_preset.setObjectName("del_preset")
        self.preset_edit = QtWidgets.QLineEdit(self.frame)
        self.preset_edit.setGeometry(QtCore.QRect(450, 330, 81, 25))
        self.preset_edit.setObjectName("preset_edit")
        self.set_player_dice_edit_char_1 = QtWidgets.QLineEdit(self.frame)
        self.set_player_dice_edit_char_1.setGeometry(QtCore.QRect(100, 300, 51, 25))
        self.set_player_dice_edit_char_1.setObjectName("set_player_dice_edit_char_1")
        self.enemy_initiative = QtWidgets.QLabel(self.frame)
        self.enemy_initiative.setGeometry(QtCore.QRect(450, 70, 61, 25))
        self.enemy_initiative.setStyleSheet("font-weight:bold")
        self.enemy_initiative.setObjectName("enemy_initiative")
        self.pushButton_clean_enemy = QtWidgets.QPushButton(self.frame)
        self.pushButton_clean_enemy.setGeometry(QtCore.QRect(450, 300, 120, 25))
        self.pushButton_clean_enemy.setObjectName("pushButton_clean_enemy")
        self.set_player_dice_edit_char_0 = QtWidgets.QLineEdit(self.frame)
        self.set_player_dice_edit_char_0.setGeometry(QtCore.QRect(100, 270, 51, 25))
        self.set_player_dice_edit_char_0.setObjectName("set_player_dice_edit_char_0")
        self.comboBox_preset = QtWidgets.QComboBox(self.frame)
        self.comboBox_preset.setGeometry(QtCore.QRect(450, 390, 73, 22))
        self.comboBox_preset.setObjectName("comboBox_preset")
        self.enemy_name_edit = QtWidgets.QLineEdit(self.frame)
        self.enemy_name_edit.setGeometry(QtCore.QRect(450, 30, 120, 25))
        self.enemy_name_edit.setObjectName("enemy_name_edit")
        self.pushButton_initiative = QtWidgets.QPushButton(self.frame)
        self.pushButton_initiative.setGeometry(QtCore.QRect(240, 390, 120, 25))
        self.pushButton_initiative.setObjectName("pushButton_initiative")
        self.comboBox_del_char = QtWidgets.QComboBox(self.frame)
        self.comboBox_del_char.setGeometry(QtCore.QRect(10, 240, 111, 22))
        self.comboBox_del_char.setObjectName("comboBox_del_char")
        self.del_character = QtWidgets.QPushButton(self.frame)
        self.del_character.setGeometry(QtCore.QRect(130, 240, 31, 22))
        self.del_character.setObjectName("del_character")
        self.set_player_dice_edit_char_2 = QtWidgets.QLineEdit(self.frame)
        self.set_player_dice_edit_char_2.setGeometry(QtCore.QRect(100, 330, 51, 25))
        self.set_player_dice_edit_char_2.setObjectName("set_player_dice_edit_char_2")
        self.edit_initiative_redaction = QtWidgets.QLineEdit(self.frame)
        self.edit_initiative_redaction.setGeometry(QtCore.QRect(10, 140, 51, 25))
        self.edit_initiative_redaction.setObjectName("edit_initiative_redaction")
        self.label_enemy_name_redaction = QtWidgets.QLabel(self.frame)
        self.label_enemy_name_redaction.setGeometry(QtCore.QRect(10, 40, 115, 25))
        self.label_enemy_name_redaction.setStyleSheet("font-weight:bold")
        self.label_enemy_name_redaction.setObjectName("label_enemy_name_redaction")
        self.label_set_player_dice_char_2 = QtWidgets.QLabel(self.frame)
        self.label_set_player_dice_char_2.setGeometry(QtCore.QRect(10, 330, 81, 25))
        self.label_set_player_dice_char_2.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_2.setObjectName("label_set_player_dice_char_2")
        self.enemy_name = QtWidgets.QLabel(self.frame)
        self.enemy_name.setGeometry(QtCore.QRect(450, 0, 120, 25))
        self.enemy_name.setStyleSheet("font-weight:bold")
        self.enemy_name.setObjectName("enemy_name")
        self.pushButton_set_redaction = QtWidgets.QPushButton(self.frame)
        self.pushButton_set_redaction.setGeometry(QtCore.QRect(10, 170, 93, 28))
        self.pushButton_set_redaction.setObjectName("pushButton_set_redaction")
        self.set_preset = QtWidgets.QPushButton(self.frame)
        self.set_preset.setGeometry(QtCore.QRect(530, 330, 41, 25))
        self.set_preset.setObjectName("set_preset")
        self.label_set_player_dice_char_1 = QtWidgets.QLabel(self.frame)
        self.label_set_player_dice_char_1.setGeometry(QtCore.QRect(10, 300, 81, 25))
        self.label_set_player_dice_char_1.setStyleSheet("font-weight:bold")
        self.label_set_player_dice_char_1.setObjectName("label_set_player_dice_char_1")
        self.pushButton_add = QtWidgets.QPushButton(self.frame)
        self.pushButton_add.setGeometry(QtCore.QRect(490, 125, 41, 20))
        self.pushButton_add.setObjectName("pushButton_add")
        self.enemy_hp = QtWidgets.QLabel(self.frame)
        self.enemy_hp.setGeometry(QtCore.QRect(520, 70, 21, 25))
        self.enemy_hp.setStyleSheet("font-weight:bold")
        self.enemy_hp.setObjectName("enemy_hp")
        self.enemy_hp_edit = QtWidgets.QLineEdit(self.frame)
        self.enemy_hp_edit.setGeometry(QtCore.QRect(510, 100, 61, 25))
        self.enemy_hp_edit.setObjectName("enemy_hp_edit")
        self.label_enemy_hp_redaction = QtWidgets.QLabel(self.frame)
        self.label_enemy_hp_redaction.setGeometry(QtCore.QRect(70, 110, 61, 25))
        self.label_enemy_hp_redaction.setStyleSheet("font-weight:bold")
        self.label_enemy_hp_redaction.setObjectName("label_enemy_hp_redaction")
        self.edit_hp_redaction = QtWidgets.QLineEdit(self.frame)
        self.edit_hp_redaction.setGeometry(QtCore.QRect(70, 140, 51, 25))
        self.edit_hp_redaction.setObjectName("edit_hp_redaction")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_delete_character.setText(_translate("MainWindow", "Delete enemy"))
        self.load_preset_2.setText(_translate("MainWindow", "Load preset"))
        self.label_enemy_initiative_redaction.setText(_translate("MainWindow", "Initiative"))
        self.label_set_player_dice_char_3.setText(_translate("MainWindow", "Character 4"))
        self.label_set_player_dice_char_0.setText(_translate("MainWindow", "Character 1"))
        self.pushButton_apply_player_dice.setText(_translate("MainWindow", "Refresh"))
        self.load_preset.setText(_translate("MainWindow", "load"))
        self.del_preset.setText(_translate("MainWindow", "del"))
        self.enemy_initiative.setText(_translate("MainWindow", "Initiative"))
        self.pushButton_clean_enemy.setText(_translate("MainWindow", "Clear"))
        self.pushButton_initiative.setText(_translate("MainWindow", "Initiative"))
        self.del_character.setText(_translate("MainWindow", "del"))
        self.label_enemy_name_redaction.setText(_translate("MainWindow", "Name"))
        self.label_set_player_dice_char_2.setText(_translate("MainWindow", "Character 3"))
        self.enemy_name.setText(_translate("MainWindow", "Name"))
        self.pushButton_set_redaction.setText(_translate("MainWindow", "redaction"))
        self.set_preset.setText(_translate("MainWindow", "set"))
        self.label_set_player_dice_char_1.setText(_translate("MainWindow", "Character 2"))
        self.pushButton_add.setText(_translate("MainWindow", "add"))
        self.enemy_hp.setText(_translate("MainWindow", "HP"))
        self.label_enemy_hp_redaction.setText(_translate("MainWindow", "HP"))







