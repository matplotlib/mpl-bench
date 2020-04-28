from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import glob
import os

import matplotlib.pyplot as plt


dirname = os.path.join(os.path.dirname(__file__), 'data')
files = sorted(os.path.basename(f)
               for f in glob.iglob(os.path.join(dirname, 'basn*.png')))


def time_pngsuite(fname):
    data = plt.imread(os.path.join(dirname, fname))
time_pngsuite.params = files
