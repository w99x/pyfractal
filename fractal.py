# coding=utf-8
g_coefs = [((1, 85), dict(a=0.85, b=0.04, c=-0.04, d=0.85, e=0, f=1.6)),
           ((86, 92), dict(a=0.2, b=-0.26, c=0.23, d=0.22, e=0, f=1.6)),
           ((93, 99), dict(a=-0.15, b=0.28, c=0.26, d=0.24, e=0, f=0.44)),
           ((100, 100), dict(a=0, b=0, c=0, d=0.16, e=0, f=0))]

def get_point(point, a, b, c, d, e, f):
    x = point[0]
    y = point[1]
    return a * x + b * y + e, c * x + d * y + f


def get_points_generator(start_point):
    import random
    import time
    random.seed(round(time.time()))
    x = start_point[0]
    y = start_point[1]
    for i in xrange(100000):
        rnd = random.randint(1, 100)
        coef = filter(lambda z: z[0][0] <= rnd <= z[0][1], g_coefs)
        x, y = get_point((x, y), **coef[0][1])
        yield x, y


import matplotlib.pyplot as plt

points = list(get_points_generator((0, 0)))
plt.plot(*zip(*points), marker='.', markersize=1, color='r', ls='')
plt.show()
