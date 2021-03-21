#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget

from utils import Point
from shapes import *


class Paint(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.reset()
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('white'))
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.show()

    def reset(self):
        self.points = []
        self.locations = defaultdict(lambda: [])
        self.isDrawing = False
        self.captured_point = None
        self.update()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        if self.parent.mode == 'Paint':
            self.draw_points(painter, self.points, Qt.black, 3)
            self.draw_figures(painter)
        else:
            self.draw_figures(painter)
            self.draw_points(painter, self.locations,
                             QColor(choice(QColor.colorNames())), 10)
        painter.end()

    def draw_points(self, painter, points, color, width):
        pen = QPen(color)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(width)
        painter.setPen(pen)

        for point in points:
            painter.drawPoint(point)

    def draw_figures(self, painter):
        for figs in self.locations.values():
            for fig in figs:
                fig.draw(painter)

    def mousePressEvent(self, event):
        pos = Point(event.pos().x(), event.pos().y())
        if not self.isDrawing:
            self.points = []
            self.update()
            self.isDrawing = True
        if self.parent.mode == 'Paint':
            brd_color = self.parent.toolbar.brd_color_btn.get_color()
            bg_color = self.parent.toolbar.bg_color_btn.get_color()
            self.points.append(pos)
            if len(self.points) == 2:
                if self.parent.active == Segment.name():
                    figure = Segment(self.points, brd_color=brd_color)
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == Ray.name():
                    figure = (Ray(self.points, brd_color=brd_color, geometry=self.geometry()))
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == Line.name():
                    figure = (Line(self.points, brd_color=brd_color, geometry=self.geometry()))
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == Circle.name():
                    figure = Circle(self.points, brd_color=brd_color, bg_color=bg_color)
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == Square.name():
                    figure = Square(self.points, brd_color=brd_color, bg_color=bg_color)
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == RegularPolygon.name():
                    figure = RegularPolygon(self.points, brd_color, bg_color, self.parent.toolbar.num)
                    self.locations[figure.get_location()].append(figure)
                else:
                    self.update()
                    return
                self.points = []
                self.isDrawing = False
            elif len(self.points) == 3 and self.parent.active != Polygon.name():
                if self.parent.active == Ellipse.name():
                    figure = Ellipse(self.points, brd_color, bg_color)
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == Rectangle.name():
                    figure = Rectangle(self.points, brd_color=brd_color, bg_color=bg_color)
                    self.locations[figure.get_location()].append(figure)
                elif self.parent.active == Rhombus.name():
                    figure = Rhombus(self.points, brd_color=brd_color, bg_color=bg_color)
                    self.locations[figure.get_location()].append(figure)
                else:
                    self.update()
                    return
                self.points = []
                self.isDrawing = False
            elif len(self.points) == self.parent.toolbar.num:
                if self.parent.active == Polygon.name():
                    figure = Polygon(self.points, brd_color=brd_color, bg_color=bg_color)
                    self.locations[figure.get_location()].append(figure)
                    self.points = []
                    self.isDrawing = False
        else:
            if self.captured_point is None:
                for point in self.locations:
                    if (point.x() - pos.x()) ** 2 + (point.y() - pos.y()) ** 2 <= 25:
                        self.captured_point = point
                        break
            else:
                figure = self.locations[self.captured_point].pop()
                if not self.locations[self.captured_point]:
                    del self.locations[self.captured_point]
                figure.move(pos)
                self.locations[pos].append(figure)
                self.captured_point = None
        self.update()
