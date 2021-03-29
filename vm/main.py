import csv
import numpy as np
import matplotlib.pyplot as plt

with open('10_NN.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    data = {}
    for line in csv_reader:
        key = int(line[0])
        #valuess = list(float(line[1].replace(',','.')),float(line[2].replace(',','.')),float(line[3].replace(',','.')))
        data[key] = []
        mean = 0
        for cnt, val1 in enumerate(line):
            val = float(val1.replace(',','.'))
            if val != 999.9:
                mean = (mean+val)/(cnt+1) 
                data[key].append(round(val,1))
            else:
                data[key].append(round(mean,1))

z5 = []
for x in data:
    d = data[x][6]
    if d < 50:
        z5.append(d)
x = np.arange(0,len(z5),1)
y = np.array(z5,dtype = float)
plt.scatter(x,y,s=7, c='red', marker="o", alpha = 0.5)

def polynom5(ans,x):
    t = 0
    for i in range(len(ans)):
        t += ans[i][0] * (x**i)
    return t

def find_coefficents_for_least_square_method(x_values,y_values):
    xi = np.array(x_values,dtype = np.float)
    yi = np.array(y_values,dtype = np.float)
    matrix_len = len(x_values)
    A = np.zeros((matrix_len,matrix_len))
    for x in range(matrix_len):
        for y in range(matrix_len):
            A[x][y] = np.sum(np.power(xi,x+y,dtype=np.float))  #составляем матрицу кэф, возводим в степень xi и суммируем до n
    v = np.zeros((matrix_len,1))
    for i in range(matrix_len):
        tmp = np.zeros(matrix_len)
        for j in range(3):
            tmp[j] = yi[j] * xi[j] ** i                             #считаем произведение всех yi на xi 
        v[i][0] = np.sum(tmp)     #суммируем yi по n
    
    return np.linalg.solve(A,v)

len1 = len(z5)

approximating_x_axis = []
approximating_y_axis = []
for i in range(1,6):
    num = len1 // 6 * i - 1
    approximating_x_axis.append(num)
    approximating_y_axis.append(z5[num])


ans = find_coefficents_for_least_square_method(approximating_x_axis,approximating_y_axis)
xi = np.array(approximating_x_axis,dtype = np.float)
yi = np.array(approximating_y_axis,dtype = np.float)
xn=np.arange(np.min(xi),np.max(xi+0.1),0.1)
yn=[polynom5(ans,i) for i in xn]
plt.plot(xn,yn)
plt.grid(True)
plt.show()
