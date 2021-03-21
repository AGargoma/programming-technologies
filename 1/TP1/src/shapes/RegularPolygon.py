#######################################################
# 
# RegularPolygon.py
# Python implementation of the Class RegularPolygon
# Generated by Enterprise Architect
# Created on:      15-Mar-2021 12:48:51 AM
# Original author: User
# 
#######################################################
from math import atan, cos, sin, pi

from PyQt5.QtGui import QPen, QBrush

from utils import distance, Point
from shapes.Polygon import Polygon


class RegularPolygon(Polygon):
    @staticmethod
    def name():
        return 'RegularPolygon'

    def __init__(self, points, brd_color, bg_color, num):
        super(RegularPolygon, self).__init__(points, brd_color, bg_color)
        self.num = num
        self.location = points[0]

    def draw(self, painter):
        painter.setPen(self.get_pen())
        painter.setBrush(QBrush(self.bg_color))
        npoints = [self.points[1]]
        r = distance(npoints[0], self.points[0])
        alpha = atan((npoints[0].y() - self.points[0].y()) / (npoints[0].x() - self.points[0].x()))
        for i in range(1, self.num):
            x = r * cos(2.0 * pi * i / self.num + alpha) + self.points[0].x()
            y = r * sin(2.0 * pi * i / self.num + alpha) + self.points[0].y()
            npoints.append(Point(x, y))
        painter.drawPolygon(*npoints)
