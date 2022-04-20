import matplotlib.pyplot as plt

from .figure import LatexFigure

__all__ = [
    'ConferencePageFigure',
    'ConferenceColumnFigure',
]

#
# Measurements
#
ICML_COLUMNWIDTH = 234.8775
ICML_TEXTWIDTH   = 487.8225

#
#
#
class ConfFigure(LatexFigure):
    def __init__(self, width, size, ratio, gridspec_kw, subplot_kw):
        super().__init__(width, size, ratio, gridspec_kw, subplot_kw)
        plt.rc('font', size=11)

class ConferenceColumnFigure(ConfFigure):
    def __init__(self,
                 size=None,
                 ratio=None,
                 gridspec_kw=None,
                 subplot_kw=None):
        super().__init__(ICML_COLUMNWIDTH,
                         size,
                         ratio,
                         gridspec_kw,
                         subplot_kw)

class ConferencePageFigure(ConfFigure):
    def __init__(self,
                 size=None,
                 ratio=None,
                 gridspec_kw=None,
                 subplot_kw=None):
        super().__init__(ICML_TEXTWIDTH,
                         size,
                         ratio,
                         gridspec_kw,
                         subplot_kw)
