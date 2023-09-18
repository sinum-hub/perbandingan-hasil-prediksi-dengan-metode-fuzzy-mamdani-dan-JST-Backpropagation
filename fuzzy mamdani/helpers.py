#join method for intervals
def join(intervals):
    return min (l[0] for l in intervals), max(l[1] for l in intervals)

#simpson method
def simpson(f, a, b, prec=3):
    area = ((b - a) / 6) * (f(a) + 4*f((a + b)/2) + f(b))
    return round(area, prec)