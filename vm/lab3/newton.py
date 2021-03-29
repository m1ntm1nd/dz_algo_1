from parsers import *
import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt

data = pars()
ROW = 2

for i in range(2, 14):
    if not data[i][ROW] == 999.9:
        dat.append(data[i][ROW])
        xs.append(data[i][0])

xs = np.array([x for x in xs])
ys = dat


def _poly_newton_coefficient(x, y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])

    return a


def newton_polynomial(x_data, y_data, x):
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p

    return p


newx = linspace(xs[0], xs[-1], 100)
newy = [newton_polynomial(xs,from parsers import *
import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt

data = pars()
ROW = 2

for i in range(2, 14):
    if not data[i][ROW] == 999.9:
        dat.append(data[i][ROW])
        xs.append(data[i][0])

xs = np.array([x for x in xs])
ys = dat


def _poly_newton_coefficient(x, y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])

    return a


def newton_polynomial(x_data, y_data, x):
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p

    return p


newx = linspace(xs[0], xs[-1], 100)
newy = [newton_polynomial(xs, ys, newx)]

plt.plot(xs, ys, 'or')

for x in newx:
    print(x, ' ', end='')
print()
for y in newy[0]:
    print(y, ' ', end='')

plt.plot(newx, newy[0])
plt.grid()
plt.show()
