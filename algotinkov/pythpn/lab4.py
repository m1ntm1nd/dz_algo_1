import matplotlib.pyplot as plt


def grad_min_sec_to_grad(items : list):
    for i in range(len(items)):
        items[i] = items[i][0]+items[i][1]/60+items[i][2]/3600 
    return  items

def main():
    x = [-1,0,1]
    temp = [
        [273,25,35],
        [273,24,24],
        [273,23,18]
        ]
    y = grad_min_sec_to_grad(temp)

    plt.scatter(x, y, s=7, c='red', marker="o", alpha = 0.5)
    plt.ylabel('X, grad', fontsize=16)
    plt.xlabel('N минимума', fontsize=16) 
    plt.minorticks_on()
    plt.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
    plt.savefig('I15.png')
    plt.show()

if __name__ == '__main__':
    main() 