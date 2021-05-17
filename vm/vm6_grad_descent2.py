import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy import abs,sqrt,exp
import matplotlib.pyplot as plt
import sys

phi = 0.5 * (1.0 + sqrt(5.0))
sys.setrecursionlimit(10**6)

def f(x1,x2,x3=-1.21682):
    f = (x1 ** 4) + 22.0 * (x1 ** 3) + 181.5 * (x1 ** 2) + 665.5 * x1 + (x2 ** 2) - 1.4 * x2 + 3* (x3 ** 2) + 10.8 * x3 + 922.7725
    return f

def dFx1(x1):
    return 4*x1**3 + 66.0*x1**2 + 363.0*x1 + 665.5
def dFx2(x2):
    return 2*x2 - 1.4
def dFx3(x3):
    return 6*x3 + 10.81

h=0.00005
def scw(F,h):
    alpha0=0
    while not((F(alpha0-h)>F(alpha0))&(F(alpha0)<F(alpha0+h))):
        if F(alpha0-h)>F(alpha0+h):
            alpha0=alpha0+h/2
        else:
            alpha0=alpha0-h/2
    return alpha0

def minimize(f,eps,a,b): 
    if abs(b - a) < eps: 
        return (a + b)/2
    else:
        t = (b - a) / phi
        x1, x2 = b - t, a + t
        if f(x1) >= f(x2):
            return minimize(f,eps,x1,b)
        else:
            return minimize(f,eps,a,x2)
h=0.5
def scw(F,h):
    alpha0=0
    while not((F(alpha0-h)>F(alpha0))&(F(alpha0)<F(alpha0+h))):
        if F(alpha0-h)>F(alpha0+h):
            alpha0=alpha0+h/2
        else:
            alpha0=alpha0-h/2
    return alpha0


def main():
    x = np.linspace(-6, -5, 300)
    y = np.linspace(0, 1, 300)



    eps1=0.1
    eps2=0.1
    xo,yo,zo=1000,1000,1000

    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 12
    fig_size[1] = 12
    plt.rcParams["figure.figsize"] = fig_size
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig = plt.figure()
    ax = plt.axes()
    ax.contour(X, Y, Z,140)

    i=0
    x,y,z = 7, -3, 4

    while sqrt((x-xo)**2+(y-yo)**2 + (z-zo)**2)>eps1:
        i+=1
        def F(alpha): 
            return f(x+alpha*(-dFx1(x)),y+alpha*(-dFx2(y)),z+alpha*(-dFx3(z)))
        
        alpha=minimize(F,eps2,0,scw(F,h))
        xo,yo=x,y
        x,y,z=x+alpha*(-dFx1(x)),y+alpha*(-dFx2(y)),z+alpha*(-dFx3(z))
        
        plt.plot([xo, x],[yo, y],'-r')

        
        plt.plot([xo, x],[yo, y],'-r')

    print('Итераций: ',i)
    plt.plot([x],[y],'-bo')
    print(x,y)                   

    plt.show() 

if __name__ == "__main__":
    main()
