from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import matplotlib.pyplot as plt


def teardown(*args, **kwargs):
    plt.close('all')


def time_subplots(n):
    fig, ax = plt.subplots(n, n)
    fig.canvas.draw()
time_subplots.params = (1, 2, 10)
time_subplots.param_names = ('n', )


def time_projection(proj):
    fig, ax = plt.subplots(subplot_kw=dict(projection=proj))
    fig.canvas.draw()
time_projection.params = ('rectilinear', 'polar',
                          'aitoff', 'hammer', 'mollweide', 'lambert')
time_projection.param_names = ('proj', )


def time_plot():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 2])
    fig.canvas.draw()


def time_savefig():
    fig, ax = plt.subplots()
    fig.savefig('time_savefig.png')
