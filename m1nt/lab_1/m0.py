import csv
import numpy as np
import matplotlib.pyplot as plt

with open('ex1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    keys = []
    data = {}
    for line in csv_reader:
        keyss = float(line[0].replace(',','.'))
        keys.append(keyss)
        ans = []
        ans.append(float(line[1].replace(',','.')))
        ans.append(float(line[2].replace(',','.')))
        ans.append(float(line[3].replace(',','.')))
        ans.append(float(line[4].replace(',','.')))
        ans.append(float(line[5].replace(',','.')))
        data[keyss] = (np.log(ans[0]/ans[1]) + np.log(ans[1]/ans[2]) + np.log(ans[2]/ans[3]) + np.log(ans[3]/ans[4]))/ 4
    
    plt.scatter(keys, list((data.values())), s=7, c='red', marker="o", alpha = 0.5, label='Декремент')  
    #plt.plot(keys,list((data.values())), marker="o", label="d")
    #     data[0][keyss] = float(line[1].replace(',','.'))
    #     data[1][keyss] = float(line[2].replace(',','.'))
    #     data[2][keyss] = float(line[3].replace(',','.'))
    # x = list(data[0].keys())
    # y = []
    # # y = list(data.values[0])
    # # y2 = list(data.values[1])
    # # y3 = list(data.values[2])
    # plt.figure(figsize=(10, 5))
    # for val in data:
    #     y.append(val)
    # plt.plot(x,list((y[0].values())),label = r"Ur")
    # plt.plot(x,list((y[1].values())),label = r"Uc")
    # plt.plot(x,list((y[2].values())),label = r"Ul")
    # #plt.errorbar(x, y, xerr=0.05, yerr=2,marker='s', mfc='red', mec='green')
    # # x2 = np.arange(1.0,16.0,0.01)
    # # y2 = np.divide(200,x2)
    # # plt.plot(np.add(x2,3),y2,label = r"$200/x-4$")
    plt.xlabel('R, Om', fontsize=16)
    plt.ylabel('d ед', fontsize=16) 
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.savefig('figure_with_legend.png')
    plt.show()