import numpy as np
import matplotlib.pyplot as plt

def f(x1,x2,x3=-1.21682):
    f = (x1 ** 4) + 22.0 * (x1 ** 3) + 181.5 * (x1 ** 2) + 665.5 * x1 + (x2 ** 2) - 1.4 * x2 + 3* (x3 ** 2) + 10.8 * x3 + 922.7725
    return f
def svenn(a,h):
    if (f(a-abs(h)) >= f(a)) and (f(a+abs(h))>= f(a)):
        return [a-abs(h), a+abs(h)]
    elif (f(a-abs(h)) >= f(a)) and (f(a+abs(h))<= f(a)):
        svenn(a+abs(h)/2, abs(h)/2)
    elif (f(a-abs(h)) < f(a)) and (f(a+abs(h)) > f(a)):
        svenn(a-abs(h)/2, -abs(h)/2)
    else:
        print('Error')

def main():
    fig, ax = plt.subplots()
    x1 = np.arange(-100, 100, 0.001)
    ax.plot(x1,f(x1,0))
    




if __name__ == '__main__':
    main() 