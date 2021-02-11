import operator as op
import itertools as it
import collections as cl

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

__all__ = [
    'OneColumnFigure',
    'TwoColumnFigure',
]

from ratio import MatplotlibRatio

Panel = cl.namedtuple('Panel', 'row, col, ax')

class ACMFigure:
    _dimensions = 2

    def __init__(self, nrows=1, ncols=1, ratio=None, **kwargs):
        if ratio is None:
            ratio = MatplotlibRatio()
        width = self.pt2in(self.width)
        height = ratio * width
        fig = plt.figure(figsize=(width, height))
        self.plots = (fig
                      .add_gridspec(nrows=nrows, ncols=ncols, **kwargs)
                      .subplots(squeeze=False))
        self._ax = None

    def __iter__(self):
        for (i, ax) in np.ndenumerate(self.plots):
            assert 0 < len(i) <= self._dimensions
            iterable = it.zip_longest(range(self._dimensions), i, fillvalue=0)
            (x, y) = map(op.itemgetter(1), iterable)
            yield Panel(x, y, ax)

    @staticmethod
    def pt2in(pt):
        return constants.point / constants.inch * pt

    @property
    def ax(self):
        if self._ax is None:
            panels = list(self)
            if len(panels) > 1:
                raise AttributeError('Too many panels to distinguish')
            self._ax = panels.pop().ax

        return self._ax

    @property
    def width(self):
        raise NotImplementedError()

class OneColumnFigure(ACMFigure):
    @property
    def width(self):
        return 241.14749

class TwoColumnFigure(ACMFigure):
    @property
    def width(self):
        return 506.295
