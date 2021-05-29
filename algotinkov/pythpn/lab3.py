import matplotlib.pyplot as plt


def grad_min_sec_to_grad(items : list):
    for i in range(len(items)):
        items[i] = items[i][0]+items[i][1]/60+items[i][2]/3600 
    return  items

def main():
    x = [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
    temp = [
        [273,31,19],
        [273,30,0],
        [273,28,50],
        [273,27,55],
        [273,26,55],
        [273,25,5],
        [273,23,42],
        [273,22,4],
        [273,20,44],
        [273,19,36],
        [273,18,42],
        [273,17,23]
        ]
    y = grad_min_sec_to_grad(temp)

    plt.scatter(x, y, s=7, c='red', marker="o", alpha = 0.5)
    plt.ylabel('X, grad', fontsize=16)
    plt.xlabel('N минимума', fontsize=16) 
    plt.minorticks_on()
    plt.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
    plt.savefig('I2.png')
    plt.show()

if __name__ == '__main__':
    main() 