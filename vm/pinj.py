import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys
from scipy.integrate import odeint

eps = 10**-12

def f(x,y):
    return -np.sqrt(3+y**2) / (np.sqrt(1-x**2) * y)


def main():
    y0 = 2
    x = np.linspace(0, 20, 30)
    y = odeint(f,y0,x)
    plt.plot(x,y)
    plt.show()
    
if __name__ == "__main__":
    main()
