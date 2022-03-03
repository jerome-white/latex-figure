import matplotlib.pyplot as plt

from .figure import LatexFigure

__all__ = [
    'ConferencePageFigure',
]

#
# Measurements
#
DATA_TEXTWIDTH = 397.48499

#
#
#
class ConferencePageFigure(LatexFigure):
    def __init__(self,
                 size=None,
                 ratio=None,
                 gridspec_kw=None,
                 subplot_kw=None):
        super().__init__(DATA_TEXTWIDTH, size, ratio, gridspec_kw, subplot_kw)
        plt.rc('font', size=10)
