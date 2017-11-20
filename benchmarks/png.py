from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import glob
import os

import matplotlib.pyplot as plt
from matplotlib import _png


dirname = os.path.join(os.path.dirname(__file__), 'data')
files = sorted(glob.iglob(os.path.join(dirname, 'basn*.png')))


def time_pngsuite(fname):
    data = plt.imread(fname)
time_pngsuite.params = files


def time_imread_png_uint16():
    img = _png.read_png_int(os.path.join(os.path.dirname(__file__),
                                         'data/uint16.png'))
