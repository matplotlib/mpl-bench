from __future__ import absolute_import, division, print_function

import distutils.version

import numpy as np

import matplotlib
import matplotlib.pyplot as plt


MPL_VERSION = distutils.version.LooseVersion(matplotlib.__version__)


class InterpolationSuite:
    params = ('none', 'nearest', 'bilinear', 'bicubic')
    param_names = ('interpolation', )

    def setup(self, interpolation):
        self.data = np.arange(100).reshape((10, 10))
        self.fig, self.ax = plt.subplots(dpi=100)
        self.ax.set_xlim(0, 3)
        self.ax.set_ylim(0, 3)

    def teardown(self, interpolation):
        plt.close(self.fig)

    def time_setup(self, interpolation):
        self.ax.imshow(self.data, interpolation=interpolation,
                       extent=(1, 2, 1, 2))

    def time_full_draw(self, interpolation):
        self.ax.imshow(self.data, interpolation=interpolation,
                       extent=(1, 2, 1, 2))
        self.fig.canvas.draw()


class MaskSuite:
    # Test mask image two ways: Using nans and using a masked array.
    params = ('nan', 'mask')
    param_names = ('method', )

    def setup(self, method):
        if method == 'nan':
            A = np.ones((5, 5))
            A[1:2, 1:2] = np.nan
        elif method == 'mask':
            A = np.zeros((5, 5), dtype=bool)
            A[1:2, 1:2] = True
            A = np.ma.masked_array(np.ones((5, 5), dtype=np.uint16), A)
        else:
            raise NotImplementedError('%s is not a known masking method' %
                                      (method, ))

        self.A = A
        self.fig, self.ax = plt.subplots(dpi=100)

    def teardown(self, method):
        plt.close(self.fig)

    def time_setup(self, method):
        self.ax.imshow(self.A, interpolation='nearest')

    def time_full_draw(self, method):
        self.ax.imshow(self.A, interpolation='nearest')
        self.fig.canvas.draw()


class TypeSuite:
    # Test both endianness, some alternate float and non-float types.
    params = ('<f8', '>f8', np.longdouble, int, bool)
    param_names = ('dtype', )

    def setup(self, t):
        if t == np.longdouble and MPL_VERSION < '2.1.0':
            raise NotImplementedError(
                'Long double not supported in this Matplotlib version')

        x = np.arange(10)
        X, Y = np.meshgrid(x, x)
        Z = ((X - 5)**2 + (Y - 5)**2)**0.5

        self.data = Z.astype(t)

        self.fig, self.ax = plt.subplots(dpi=100)

    def teardown(self, t):
        if t == np.longdouble and MPL_VERSION < '2.1.0':
            return

        plt.close(self.fig)

    def time_setup(self, t):
        self.ax.imshow(self.data)

    def time_full_draw(self, t):
        self.ax.imshow(self.data)
        self.fig.canvas.draw()
