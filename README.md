# ACM Figure

A library that manages plot formatting when building figures in
Matplotlib specifically for the ACM template.

## Usage

Download and setup the environment:
```bash
$> git clone https://github.com/jerome-white/acm-figure
$> cd acm-figure
$> export MATPLOTLIBRC=`pwd`
$> export PYTHONPATH=`pwd`
```

The include the module. For example:
```python
from acmfig import OneColumnFigure
```

## Issues

For now only `sigconf` is supported.
