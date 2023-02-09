from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QLabel
from PyQt6.QtCore import Qt, QPointF, QRect
from PyQt6.QtGui import QGuiApplication, QPixmap


class TokenObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r, type):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        if type:
            self.setBrush(Qt.GlobalColor.red)
        else:
            self.setBrush(Qt.GlobalColor.blue)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(QPointF(updated_cursor_x, updated_cursor_y))

    def mouseReleaseEvent(self, event):
        print(f'x: {self.pos().x()}, y: {self.pos().y()}')