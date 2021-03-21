import math

from PyQt5.QtCore import QPoint


def distance(p1, p2):
    return math.hypot(p1.x() - p2.x(), p1.y() - p2.y())


def create_line(p1, p2):
    def line(x):
        k = (p2.y() - p1.y()) / (p2.x() - p1.x())
        b = p1.y() - p1.x() * k
        return k * x + b

    return line


def mbr(points):
    minx = min(list(map(lambda p: p.x(), points)))
    miny = min(list(map(lambda p: p.y(), points)))
    maxx = max(list(map(lambda p: p.x(), points)))
    maxy = max(list(map(lambda p: p.y(), points)))
    return (minx, miny), (maxx, maxy)


class Point(QPoint):
    def __init__(self, x, y):
        super(Point, self).__init__(x, y)

    def __hash__(self):
        return hash((self.x(), self.y()))
