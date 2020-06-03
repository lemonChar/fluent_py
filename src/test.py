import collections

#Point = collections.namedtuple('Point', 'x import', rename=True)
#p = Point(1, 2)

Point = collections.namedtuple('Point', 'x y z', defaults=[4, 6])
p = Point(x=1)

print(p.__repr__())
