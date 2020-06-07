import collections
from random import choice


#Point = collections.namedtuple('Point', 'x import', rename=True)
#p = Point(1, 2)

Point = collections.namedtuple('Point', 'x y z', defaults=[4, 6])
p = Point(x=1)

print(p.__repr__())


class Test:
    def __init__(self, a, b):
        self.c = a
        self.d = b
        self.count = 1

    def print_test(self):
        print(self)
        print(self.__class__)

    def __len__(self):
        return 2


t = Test(3, 4)

t.print_test()
print(len(t))

print(t.c, t.count, t.d)

ranks = [str(n) for n in range(2, 11)] + list('JQKA')

test_tuple = [tuple([a, b, 0]) for a in range(1, 5) for b in range(6, 10)]

print(choice(test_tuple))

# for t in test_tuple:
#     print(t)

test_t = tuple([1, 2, 0])
print(test_t[-1])

str = '12 2311 4523 345'
strs = str.split()
for s in strs:
    print(s)

#suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}


sort_suit = sorted(suit_values, key=lambda x: suit_values[x])

print(sort_suit)


def m(k=[]):
    k += [1]
    print(k, end=" ")


for i in range(5):
    m()
