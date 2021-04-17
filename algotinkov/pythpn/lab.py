import matplotlib.pyplot as plt

x = [0,100,220,350,540,860,1600,2400]
y = [240,220,240,238,238,240,239,240]

plt.scatter(x, y, s=7, c='red', marker="o", alpha = 0.5)
plt.xlabel('R, Om', fontsize=16)
plt.ylabel('T мкс', fontsize=16) 
plt.minorticks_on()
plt.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
plt.savefig('period.png')
plt.show()
