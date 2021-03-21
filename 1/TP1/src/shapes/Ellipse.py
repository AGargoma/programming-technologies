#######################################################
# 
# Ellipse.py
# Python implementation of the Class Ellipse
# Generated by Enterprise Architect
# Created on:      15-Mar-2021 12:48:51 AM
# Original author: User
# 
#######################################################
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPen, QBrush

from utils import distance, mbr, Point
from shapes.Shape import Shape


class Ellipse(Shape):
    @staticmethod
    def name():
        return 'Ellipse'

    def __init__(self, points, brd_color, bg_color):
        if len(points) > 2:
            points = [Point(*p) for p in mbr(points)]
            self._radx = (points[1].x() - points[0].x()) / 2
            self._rady = (points[1].y() - points[0].y()) / 2
            self.location = Point(points[0].x() + self._radx,
                                  points[0].y() + self._rady)
        else:
            self._radx = distance(points[0], points[1])
            self._rady = self._radx
            self.location = points[0]
        super(Ellipse, self).__init__(points, brd_color, bg_color)

    def draw(self, painter):
        painter.setPen(self.get_pen())
        painter.setBrush(QBrush(self.bg_color))
        painter.drawEllipse(QRect(self.location.x() - self._radx,
                                  self.location.y() - self._rady,
                                  2 * self._radx, 2 * self._rady))