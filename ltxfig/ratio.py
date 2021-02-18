import math
import operator as op
import functools as ft

from scipy import constants

__all__ = [
    'GoldenRatio',
    'MatplotlibRatio',
]

class PlotRatio:
    def __init__(self, wscale, hscale, ratio):
        self.wscale = wscale
        self.hscale = hscale
        self.ratio = ratio

    def __call__(self, width):
        w = self.wscale * width
        h = w * self.ratio * self.hscale

        return (w, h)

class GoldenRatio(PlotRatio):
    def __init__(self, wscale=1, hscale=1):
        super().__init__(wscale, hscale, constants.golden)

class MatplotlibRatio(PlotRatio):
    _default = (
        6.4, # width
        4.8, # height
    )

    def __init__(self, wscale=1, hscale=1):
        wh_ratio = op.truediv(*self._default)
        super().__init__(wscale, hscale, wh_ratio)
