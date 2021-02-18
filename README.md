# Latex Figure

A library that manages plot formatting when building figures in
Matplotlib to be presented in Latex-backed publications.

## Usage

Download and setup the environment:
```bash
$> git clone https://github.com/jerome-white/latex-figure
$> cd latex-figure
$> export PYTHONPATH=`pwd`
```

### Example: ACM with PGF

This library was designed primarily for making clean figures for ACM
publications.

1. One of the best file types for ACM -- and most other -- Latex
   documents is PGF. A matplotlibrc file tailored to this situation is
   included in this repository:
   ```bash
   $> export MATPLOTLIBRC=`pwd`/matplotlibrc/pgf.rc
   ```

2. Import the class type corresponding to the type of figure you
   want. An example from the ACM module:
   ```python
   from ltxfig.acm import ConferenceColumnFigure

   panels = ConferenceColumnFigure()
   ```

3. While `ConferenceColumnFigure` can be used with its defaults, it is
   sometimes handy to change the number of panels (size) or plot
   dimensions:
   ```python
   from ltxfig import MatplotlibRatio, PlotSize

   size = PlotSize(3, 4) # three rows, four columns
   ratio = MatplotlibRatio(hscale=0.5) # reduce the height be half
   panels = ConferenceColumnFigure(size=size, ratio=ratio)
   ```

## Issues

For now only ACM "sigconf" is supported.
