

def mamdani(degree, fs, z):
    return min(degree, fs.func(z))

def larsen(degree, fs, z):
    return degree * fs.func(z)
