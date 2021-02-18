from .figure import LatexFigure

__all__ = [
    'ConferencePageFigure',
    'ConferenceColumnFigure',
]

#
# Measurements
#
SIGCONF_COLUMNWIDTH = 241.14749
SIGCONF_TEXTWIDTH   = 506.295

#
#
#
class ConferenceColumnFigure(LatexFigure):
    def __init__(self,
                 size=None,
                 ratio=None,
                 gridspec_kw=None,
                 subplot_kw=None):
        super().__init__(SIGCONF_COLUMNWIDTH,
                         size,
                         ratio,
                         gridspec_kw,
                         subplot_kw)

class ConferencePageFigure(LatexFigure):
    def __init__(self,
                 size=None,
                 ratio=None,
                 gridspec_kw=None,
                 subplot_kw=None):
        super().__init__(SIGCONF_TEXTWIDTH,
                         size,
                         ratio,
                         gridspec_kw,
                         subplot_kw)
