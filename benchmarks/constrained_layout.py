from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np

import matplotlib.pyplot as plt


def time_subplots(n):
    fig, ax = plt.subplots(n, n, constrained_layout=True)
    fig.canvas.draw()
time_subplots.params = (1, 2, 5)
time_subplots.param_names = ('n', )


def time_subplots_colorbar(n):
    fig, axs = plt.subplots(n, n, figsize=(10, 10), constrained_layout=True,
                            squeeze=False)
    for ax in axs.flat:
        pc = ax.pcolormesh(np.random.randn(20, 20))
        fig.colorbar(pc, ax=ax)
    fig.canvas.draw()
time_subplots_colorbar.params = (1, 2, 5)
time_subplots_colorbar.param_names = ('n', )
