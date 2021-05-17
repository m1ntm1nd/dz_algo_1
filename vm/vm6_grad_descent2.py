import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
import matplotlib.pyplot as plt

phi = 0.5 * (1.0 + sqrt(5.0))

def f(x1,x2,x3=-1.21682):
    return (x1 ** 4) + 22.0 * (x1 ** 3) + 181.5 * (x1 ** 2) + 665.5 * x1 +  2 *(x2 ** 2) - 1.4 * x2# + 3* (x3 ** 2) + 10.8 * x3 + 922.7725

def gradx(x1,x2):
    return 4*x1**3 + 66.0*x1**2 + 363.0*x1 + 665.5

def grady(x1,x2):
    return 4*x2 - 1.4


x,y= 7, -3


h=0.05

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

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 12
plt.rcParams["figure.figsize"] = fig_size

xmin,xmax=-6,-5
ymin,ymax=0,1
X = np.arange(xmin,xmax, 0.01)
Y = np.arange(ymin,ymax, 0.01)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes()
ax.contour(X, Y, Z,140)
eps1=0.0001
eps2=0.0001
xo,yo=1000,1000
i=0


while sqrt((x-xo)**2+(y-yo)**2)>eps1:
    i+=1
    def F(alpha): 
        return f(x+alpha*(-gradx(x,y)),y+alpha*(-grady(x,y)))
    
    alpha=minimize(F,eps2,0,scw(F,h))
    xo,yo=x,y
    x,y=x+alpha*(-gradx(x,y)),y+alpha*(-grady(x,y))
    
    plt.plot([xo, x],[yo, y],'-r')

print('Итераций: ',i)
plt.plot([x],[y],'-bo')
print(x,y)
plt.show()