import csv
import numpy as np
import matplotlib.pyplot as plt



keys = [0, 100, 220, 350, 540, 860, 1600, 2400]

data = [680, 660, 480, 460, 360, 300, 240, 120]

plt.scatter(keys, data, s=7, c='red', marker="o", alpha = 0.5)  

plt.xlabel('R, Om', fontsize=16)
plt.ylabel('T мкс', fontsize=16) 
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend1.png')
plt.show()