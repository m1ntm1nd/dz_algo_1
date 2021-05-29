import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from scipy import interpolate
from scipy.optimize import minimize, rosen
import sys
sys.setrecursionlimit(10**6)

def f(x1 = -1.21682,x2 = 0.83666,x3=-1.21682):
    #f = (x1 ** 4) + 22.0 * (x1 ** 3) + 181.5 * (x1 ** 2) + 665.5 * x1 + (x2 ** 2) - 1.4 * x2 + 3* (x3 ** 2) + 10.8 * x3 + 922.7725
    f = x1**2+10*x1+6
    return f


def slide_window(x0,h,func):
    if (func(x0-h) > func(x0) < func(x0+h)):
        print(func(x0))
        return [x0-h, x0+h] 
    if func(x0 - h) > func(x0 + h):        
        return slide_window(x0+h/2,h,func)
    elif func(x0 + h) >= func(x0 - h):
        return slide_window(x0-h/2,h,func)

def quadratic_interpolation(x_coords,func):
    # x = np.arange(x_coords[0],x_coords[1], 0.1)
    # y = func(x)
    # f_quadratic = interpolate.interp1d(x, y, kind = 'quadratic')
    # fig, ax = plt.subplots()
    # t = x[0]
    # prev = func(t)
    # while func(x) - prev > 10**-3:
    return (x_coords[0] + x_coords[1]) / 2


def main():
    fig, ax = plt.subplots()
    x1 = np.arange(-100, 100, 0.001)
    ax.plot(x1,f(x1))
    x_coords = slide_window(50,10,f)
    t = quadratic_interpolation(x_coords,f) 
    ax.scatter(t,f(t))
    ax.scatter(x_coords[0],f(x_coords[0]))
    ax.scatter(x_coords[1],f(x_coords[1]))
    print(f(x_coords[0]))
    print(f(x_coords[1]))
    plt.show()


if __name__ == "__main__":
    main()
