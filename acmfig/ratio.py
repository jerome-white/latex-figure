import math
import operator as op

__all__ = [
    'OneColumnFigure',
    'TwoColumnFigure',
]

class PlotRatio:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def __mul__(self, other):
        w = self.width * other
        h = self.height * float(self)

        return w * h

    def __float__(self):
        raise NotImplementedError()

class GoldenRatio(PlotRatio):
    def __float__(self):
        return (1 + math.sqrt(5)) / 2

class MatplotlibRatio(PlotRatio):
    _default = (
        6.4, # width
        4.8, # height
    )

    def __float__(self):
        return op.truediv(*self._default)
