import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2, x3=0):
    func = (x1 ** 4) + 22.0 * (x1 ** 3) + 181.5 * (x1 ** 2) + 665.5 * x1 + (x2 ** 2) - 1.4 * x2 + 3* (x3 ** 2) + 10.8 * x3 + 922.7725
    return func

x, y = np.mgrid[-3*np.pi:3*np.pi:300j,
                -3*np.pi:3*np.pi:300j]


fig, axes = plt.subplots()

#  Задаем значение каждого уровня:
lev = [0, 2, 3, 4, 6, 10, 20, 40, 100, 900]

#  Контуры одного цвета:
axes.contour(f(x,y),x,y, levels = 0)
axes.contour(f(x,y,1),x,y, levels = 20)

fig.set_figwidth(12)    #  ширина и
fig.set_figheight(6)    #  высота "Figure"

plt.show()