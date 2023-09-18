from fuzzyset import fuzzySet
from helpers import *

#mean of maximun method
def MOM(fs : fuzzySet):
    values = []
    max_value = 0

    left, right = fs.domain

    for i in range(left, right + 1):
        v = fs.func(i)
        if v == max_value:
            values.append(i)
        elif max_value < v:
            max_value = v
            values = [i]

    return sum(values) / len(values)

#center of area method
def COA(fs: fuzzySet):
    left, right = fs.domain
    n, d = 0, 0
    for i in range(left, right):
        v = fs.func(i)
        n += i * v
        d += v
    return n / d    

#bisector of area
def BOA(fs: fuzzySet):
    
    left, right = fs.domain
    m = (left + right)/2

    while True:
        l = simpson(fs.func, left, m, 10)
        r = simpson(fs.func, m, right, 10)

        if l == r:
            return m
        elif l < r:
            right = m
        else:
            left = m

        m = (left + right) /2 