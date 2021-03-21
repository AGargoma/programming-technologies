#######################################################
# 
# Polygon.py
# Python implementation of the Class Polygon
# Generated by Enterprise Architect
# Created on:      15-Mar-2021 12:48:51 AM
# Original author: User
# 
#######################################################

from PyQt5.QtGui import QPen, QBrush

from shapes.Shape import Shape


class Polygon(Shape):
    @staticmethod
    def name():
        return 'Polygon'

    def __init__(self, points, brd_color, bg_color):
        super(Polygon, self).__init__(points, brd_color, bg_color)
        self.location = points[0]

    def draw(self, painter):
        painter.setPen(self.get_pen())
        painter.setBrush(QBrush(self.bg_color))
        painter.drawPolygon(*self.points)