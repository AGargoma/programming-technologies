#######################################################
# 
# Ray.py
# Python implementation of the Class Ray
# Generated by Enterprise Architect
# Created on:      15-Mar-2021 12:48:51 AM
# Original author: User
# 
#######################################################
from PyQt5.QtGui import QPen

from utils import create_line, Point
from shapes.Line import Line


class Ray(Line):
    @staticmethod
    def name():
        return 'Ray'

    def draw(self, painter):
        painter.setPen(self.get_pen())
        p1, p2 = self.points[0], self.points[1]
        dx, dy = p2.x() - p1.x(), p2.y() - p1.y()
        if p1.y() == p2.y() and p2.x() == p1.x():
            painter.drawPoint(p1.x(), p1.y())
        elif p1.x() == p2.x():
            if dy > 0:
                painter.drawLine(p1, Point(p1.x(), self.geometry.bottom()))
            else:
                painter.drawLine(p1, Point(p1.x(), self.geometry.top()))
        else:
            line = create_line(p1, p2)
            if dx > 0:
                painter.drawLine(p1, Point(self.geometry.right(),
                                           line(self.geometry.right())))
            else:
                painter.drawLine(p1, Point(self.geometry.left(),
                                           line(self.geometry.left())))