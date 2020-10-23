from __future__ import absolute_import, division, print_function

import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.transforms as mtransforms


class BasicSuite:
    params = [[
        ('TransformNode', ),
        ('Bbox', [[0, 1], [2, 3]]),
        ('Bbox.unit', ),
        ('Bbox.null', ),
        ('Bbox.from_bounds', 0, 1, 2, 3),
        ('Bbox.from_extents', 0, 1, 2, 3),
        ('TransformedBbox', 'bbox', 'affine1'),
        ('LockableBbox', 'bbox'),
        ('Transform', ),
        ('TransformWrapper', 'affine1'),
        ('AffineBase', ),
        ('Affine2D', ),
        ('Affine2D.from_values', 1, 2, 3, 4, 5, 6),
        ('Affine2D.identity', ),
        ('IdentityTransform', ),
        ('BlendedGenericTransform', 'affine1', 'affine2'),
        ('BlendedAffine2D', 'affine1', 'affine2'),
        ('CompositeGenericTransform', 'affine1', 'affine2'),
        ('CompositeAffine2D', 'affine1', 'affine2'),
        ('BboxTransform', 'bbox', 'bbox'),
        ('BboxTransformTo', 'bbox'),
        ('BboxTransformToMaxOnly', 'bbox'),
        ('BboxTransformFrom', 'bbox'),
        ('ScaledTranslation', 1, 1, 'affine1'),
        ('TransformedPath', 'path', 'affine1'),
        ('TransformedPatchPath', 'patch'),
    ]]
    param_names = ('name_and_args', )

    def setup(self, name_args):
        name = name_args[0]
        obj = mtransforms
        for name in name_args[0].split('.'):
            try:
                obj = getattr(obj, name)
            except AttributeError:
                raise NotImplementedError(
                    '%s is not supported by this version of Matplotlib.' % (
                        name_args[0], ))
        self.init = obj

        args = []
        for arg in name_args[1:]:
            if isinstance(arg, str):
                # arg.frozen() ensures TransformNode's are valid and won't
                # count in timing.
                if arg == 'affine1':
                    arg = mtransforms.Affine2D.from_values(1, 0, 0, 4, 5, 6)
                    arg.frozen()
                elif arg == 'affine2':
                    arg = mtransforms.Affine2D.from_values(6, 0, 0, 3, 2, 1)
                    arg.frozen()
                elif arg == 'bbox':
                    arg = mtransforms.Bbox([[0, 1], [2, 3]])
                    arg.frozen()
                elif arg == 'patch':
                    arg = mpatches.Rectangle((0, 0), 1, 1)
                elif arg == 'path':
                    arg = mpath.Path.unit_rectangle()
                else:
                    raise NotImplementedError('%s is an unknown argument.' % (
                        arg, ))
            args.append(arg)
        self.args = args

    def time_creation(self, name_args):
        self.init(*self.args)

    def time_frozen(self, name_args):
        obj = self.init(*self.args)
        obj.frozen()


class BboxSetSuite:
    params = [[
        # self intersection -> no change
        (0, 0, 1, 1),
        # simple intersection
        (0.5, 0.5, 1.5, 1.5),
        # r3 contains r2
        (0.5, 0, 0.75, 0.75),
        # no intersection
        (0.5, 1.5, 1, 2.5),
        # single point
        (1, 1, 2, 2),
    ]]
    param_names = ('extent', )

    def setup(self, extent):
        self.bbox1 = mtransforms.Bbox.from_extents(0, 0, 1, 1)
        self.bbox2 = mtransforms.Bbox.from_extents(*extent)

    def time_bbox_intersection(self, extent):
        mtransforms.Bbox.intersection(self.bbox1, self.bbox2)

    def time_bbox_union(self, extent):
        mtransforms.Bbox.union((self.bbox1, self.bbox2))
