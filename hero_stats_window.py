from PyQt6 import QtCore, QtGui, QtWidgets
from hero_stats_window_ui import HeroStatsUi


class HeroStats(QtWidgets.QMainWindow, HeroStatsUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def enterEvent(self, event):
        self.show()

    def leaveEvent(self, event):
        self.hide()
