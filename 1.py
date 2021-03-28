import numpy as np
import matplotlib.pyplot as plt


def _poly_newton_coefficient(x, y):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    m = len(x)

    x = np.copy(x)

    a = np.copy(y)
    print(a)
    for k in range(1, m):
        a[m:k:-1] = (a[m:k:-1] - a[k - 1])/(x[m:k:-1] - x[k - 1])
        #print((x[k:m] - x[k - 1]))
        #print(a)
    return a

#coef = _poly_newton_coefficient([1,2,3,4,5,6],[-10.9, -5.5, -9.6, -8.7, -11.3, -13.4])

def newton_polynomial(x_data, y_data, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1  # Degree of polynomial
    #p = a[0]
    mnoj = (x-x_data[0])
    mnojM1 = [(x-x_data[n])]
    for k in range(1,n+1):
        #p += a[k]*mnoj
        mnoj *= x - x_data[k]
        mnojM1.append(mnoj)

    p = a[n]

    for k in range(1,n+1):
        p += a[n-k+1]*mnojM1[n-k+1]

        

    return p





ans = [-10.9, -5.5, -9.6, -8.7, -11.3, -13.4]
x1=np.array([1,2,3,4,5,6], dtype=float)
y1=np.array(ans, dtype=float)
xn=np.arange(np.min(x1),np.max(x1+0.1),0.1)
plt.scatter(x1,y1,s=20, c='blue', marker="o")
yn=[newton_polynomial(x1,y1,i) for i in xn]
#print(yn)
plt.scatter(xn,yn,s=7, c='red', marker="o", alpha = 0.5)
plt.grid(True)
plt.show()
if __name__ == '__main__':
    main()