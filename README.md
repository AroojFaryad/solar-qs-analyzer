# Solar Quiet Sun (QS) Intensity Analyzer

A Python tool to compute mean intensities in solar Quiet Sun regions from spectral observations.

## Quick Start

Load!
import numpy as np
from astropy.io import fits
import os

## Data Preparation
Create this structure for each observation date:
```
20140614/
├── wings.fits      # Spectral data cube
└── qs.txt         # Quiet Sun coordinates (x1,x2,y1,y2)
```

## How It Works
1. Loads coordinates from `qs.txt`
2. Extracts the QS region from `wings.fits` 
3. Computes the mean intensity
