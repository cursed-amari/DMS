# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtWidgets

from constants import *
import random

from initializing_windows.too_many_generators_class import Ui_MainWindow_too_many_generators


class MainWindow_too_many_generators(QtWidgets.QMainWindow, Ui_MainWindow_too_many_generators):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aplication_func()
        self.status = 0

    def aplication_func(self):
        # pushButton
        self.pushButton_random.clicked.connect(self.random_choice)
        self.pushButton_open_full_txt.clicked.connect(self.full_test_open)
        # method
        self.update_choose_generater()

    def update_choose_generater(self):
        generators = (
            "100 случайных событий", "666 идей энкаутеров", "101 идея локаций и приключений", "150 сюжетных поворотов",
            "100 механик босов")
        for i in generators:
            self.comboBox_choose_generater.addItem(i)

    def random_choice(self):
        if self.comboBox_choose_generater.currentText() == "100 случайных событий":
            self.textEdit_text_generator.setText(random.choice(RANDOM_EVENT))
        if self.comboBox_choose_generater.currentText() == "666 идей энкаутеров":
            self.textEdit_text_generator.setText(random.choice(IDIA_ENCOUNTERS))
        if self.comboBox_choose_generater.currentText() == "101 идея локаций и приключений":
            self.textEdit_text_generator.setText(random.choice(IDEA_LOCATIONS_AND_ADVENTURE))
        if self.comboBox_choose_generater.currentText() == "150 сюжетных поворотов":
            self.textEdit_text_generator.setText(random.choice(SCENARIO_TWIST))
        if self.comboBox_choose_generater.currentText() == "100 механик босов":
            self.textEdit_text_generator.setText(random.choice(BOSS_MECHANICS))

    def full_test_open(self):
        if self.comboBox_choose_generater.currentText() == "100 случайных событий":
            self.textEdit_text_generator.setText("\n".join(RANDOM_EVENT))
        if self.comboBox_choose_generater.currentText() == "666 идей энкаутеров":
            self.textEdit_text_generator.setText("\n".join(IDIA_ENCOUNTERS))
        if self.comboBox_choose_generater.currentText() == "101 идея локаций и приключений":
            self.textEdit_text_generator.setText("\n".join(IDEA_LOCATIONS_AND_ADVENTURE))
        if self.comboBox_choose_generater.currentText() == "150 сюжетных поворотов":
            self.textEdit_text_generator.setText("\n".join(SCENARIO_TWIST))
        if self.comboBox_choose_generater.currentText() == "100 механик босов":
            self.textEdit_text_generator.setText("\n".join(BOSS_MECHANICS))
