from collections import namedtuple


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()
    _make = classmethod(tuple.__new__)
