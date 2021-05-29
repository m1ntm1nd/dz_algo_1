import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy import abs,sqrt,exp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
phi = 0.5 * (1.0 + sqrt(5.0))

def f(x1, x2 = 0.83666, x3=-1.21682):
    f = (x1 ** 4) + 22.0 * (x1 ** 3) + 50 * (x1 ** 2) + 50 * x1 + (x2 ** 2) - 1.4 * x2# + 3* (x3 ** 2) + 10.8 * x3 + 922.7725
    return f


def dFx1(x1):
    return 4*x1**3 + 66.0*x1**2 + 100*x1 + 50
def dFx2(x2):
    return 2*x2 - 1.4

h=0.5
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

x,y = 30, 1
a_plt = np.arange(-30, 30, 0.1)
b_plt = np.arange(-30, 30, 0.1)
f_plt = np.array([[f(a, b) for a in a_plt] for b in b_plt])


fig = plt.figure()
ax = Axes3D(fig)

a, b = np.meshgrid(a_plt, b_plt)
ax.plot_surface(a, b, f_plt, color='y', alpha=0.5)

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('f')
point = ax.scatter(x, y, f(x, y), c='red')
eps1=0.1
eps2=0.0001
xo,yo=1000,1000                   
i=0
eps1=0.0001
eps2=0.0001
xo,yo=1000,1000                   
i=0
while sqrt((x-xo)**2+(y-yo)**2)>eps1:
    i+=1
    def F(alpha): 
        return f(x+alpha*(-dFx1(x)),y+alpha*(-dFx2(y)))
    
    alpha=minimize(F,eps2,0.00001,scw(F,h))
    xo,yo=x,y
    x,y=x+alpha*(-dFx1(x)),y+alpha*(-dFx2(y))
    
    ax.scatter(x, y, f(x, y), c='red')

    
    #name = str(i)+'.png'
    #plt.savefig(name)

plt.savefig('foo1.png')

