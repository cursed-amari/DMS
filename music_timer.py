from PyQt6.QtCore import QThread, pyqtSignal


class MusicTimer(QThread):
    signal = pyqtSignal(int)  # Определение сигнала

    def __init__(self, parent=None):
        super().__init__(parent)
        self.length = 0
        self.is_running = True

    def run(self):
        self.counter = 0
        while self.is_running and self.counter != self.length:
            self.signal.emit(self.counter)
            self.counter += 1
            self.sleep(1)

    def stop(self):
        self.is_running = False