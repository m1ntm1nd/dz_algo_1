import numpy as np
import matplotlib.pyplot as plt

def f(x1):
    f =  (x1 ** 3) + 181.5 * (x1 ** 2) + 665.5 * x1
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

N = 20
xx = -25

x_plt = np.arange(-100, 100, 0.001)
f_plt = [f(x) for x in x_plt]

plt.ion()   # включение интерактивного режима отображения графиков
fig, ax = plt.subplots()    # Создание окна и осей для графика
ax.grid(True)   # отображение сетки на графике

ax.plot(x_plt, f_plt)                   # отображение параболы
point = ax.scatter(xx, f(xx), c='red')  # отображение точки красным цветом

# for i in range():
#     xx = xx - lmd*df(xx)    # изменение аргумента на текущей итерации

#     point.set_offsets([xx, f(xx)])  # отображение нового положения точки

#     # перерисовка графика и задержка на 20 мс
#     fig.canvas.draw()
#     fig.canvas.flush_events()
#     time.sleep(0.02)

plt.ioff()   # выключение интерактивного режима отображения графиков

print(xx)
ax.scatter(xx, f(xx), c='blue')
plt.show()