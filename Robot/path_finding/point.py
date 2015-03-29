from collections import namedtuple


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()
    _make = classmethod(tuple.__new__)


class Point3D(namedtuple('Point3D', 'x y z')):
    __slots__ = ()
    _make = classmethod(tuple.__new__)
