#######################################################
# 
# Segment.py
# Python implementation of the Class Segment
# Generated by Enterprise Architect
# Created on:      15-Mar-2021 12:48:51 AM
# Original author: User
# 
#######################################################
from PyQt5.QtGui import QPen

from shapes.Ray import Ray


class Segment(Ray):
    @staticmethod
    def name():
        return 'Segment'

    def draw(self, painter):
        painter.setPen(self.get_pen())
        painter.drawLine(self.points[0], self.points[1])
