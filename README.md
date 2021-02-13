# ACM Figure

A library that manages plot formatting when building figures in
Matplotlib to be presented in documents using ACM Latex templates.

## Usage

Download and setup the environment:
```bash
$> git clone https://github.com/jerome-white/acm-figure
$> cd acm-figure
$> export MATPLOTLIBRC=`pwd`
$> export PYTHONPATH=`pwd`
```

Then include the module. For example:
```python
from acmfig import OneColumnFigure
```

## Issues

For now only `sigconf` is supported.
