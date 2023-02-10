from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtCore import Qt, QPointF, QRect
from PyQt6.QtGui import QGuiApplication, QPixmap, QPainter, QFont


class TokenImg(QGraphicsPixmapItem):
    """
    Объект токена для QGraphicsScene
    x, y: Кординаты
    r: Размер
    who: False(синий) True(красный)
    num: Номер токена
    """
    def __init__(self, x, y, r, who, num):
        super().__init__()
        self.setPos(x, y)
        if who:
            self.setPixmap(QPixmap(
                "img/token/token-" + num + ".png").scaled(r, r,
                                                          aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                                          transformMode=Qt.TransformationMode.SmoothTransformation))
        else:
            self.setPixmap(QPixmap(
                "img/token/token.hero-" + num + ".png").scaled(r, r,
                                                               aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                                               transformMode=Qt.TransformationMode.SmoothTransformation))

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
