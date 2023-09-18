from fuzzyset import fuzzySet
from math import sqrt

class TriangularFuzzyNumber(fuzzySet):

    def __init__(self, left, m, right):
        super().__init__(self._func, (left, right))
        self.left = left
        self.right = right
        self.m = m

    def _func(self, x):
        if x < self.left or x > self.right:
            return 0
        if x >= self.left and x <= self.m:
            return (x - self.left) / (self.m - self.left)
        if x >= self.m and x <= self.right:
            return (self.right - x) / (self.right - self.m)
        return 0

class TrapezoidalFuzzyNumber(fuzzySet):

    def __init__(self, left, m1, m2, right):
        super().__init__(self._func, (left, right))
        self.left = left
        self.m1 = m1
        self.m2 = m2
        self.right = right

    def _func(self, x):
        if x < self.left or x > self.right:
            return 0
        if x >= self.left and x < self.m1:
            return (x - self.left) / (self.m1 - self.left)
        if x >= self.m1 and x <= self.m2:
            return 1
        if x > self.m2 and x <= self.right:
            return (self.right - x)/ (self.right - self.m2)
        return 0