import operator as op
import itertools as it
import collections as cl

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

from .ratio import MatplotlibRatio

__all__ = [
    'PlotSize',
    'ACMFigure',
]

PlotSize = cl.namedtuple('PlotSize', 'row, col')
Panel = cl.namedtuple('Panel', 'pos, ax')

#
#
#
class LayoutStrategy:
    def __call__(self, width, size, ratio, gridspec_kw, subplot_kw):
        raise NotImplementedError()

class SubplotLayoutStrategy(LayoutStrategy):
    def __call__(self, width, size, figsize, plot_kw):
        (fig, axes) = plt.subplots(nrows=size.row,
                                   ncols=size.col,
                                   squeeze=False,
                                   **subplot_kw,
                                   gridspec_kw=gridspec_kw)
        fig.set_size_inches(figsize)

        return axes

class GridspecLayoutStrategy(LayoutStrategy):
    def __call__(self, width, size, figsize, gridspec_kw, subplot_kw):
        fig = plt.figure(figsize=figsize, constrained_layout=True)
        return (fig
                .add_gridspec(nrows=size.row, ncols=size.col, **gridspec_kw)
                .subplots(squeeze=False, **subplot_kw))

#
#
#
class ACMFigure:
    def __init__(self,
                 width,
                 size=None,
                 ratio=None,
                 gridspec_kw=None,
                 subplot_kw=None):
        #
        # handle defaults
        #
        if size is None:
            size = PlotSize(1, 1)

        if ratio is None:
            ratio = MatplotlibRatio()

        if gridspec_kw is None:
            gridspec_kw = {}

        if subplot_kw is None:
            subplot_kw = {}

        #
        # plots
        #
        layout = GridspecLayoutStrategy()
        figsize = ratio(self.pt2in(width))
        self.axes = layout(width, size, figsize, gridspec_kw, subplot_kw)

        #
        # others
        #
        self._ax = None

    def __iter__(self):
        dimensions = len(PlotSize._fields)
        for (i, ax) in np.ndenumerate(self.axes):
            assert 0 < len(i) <= dimensions

            iterable = it.zip_longest(range(dimensions), i, fillvalue=0)
            size = PlotSize(*map(op.itemgetter(1), iterable))

            yield Panel(size, ax)

    @property
    def ax(self):
        if self._ax is None:
            for i in self:
                if self._ax is not None:
                    raise AttributeError('Too many panels')
                self._ax = i.ax

        return self._ax

    @staticmethod
    def pt2in(pt):
        return constants.point / constants.inch * pt
