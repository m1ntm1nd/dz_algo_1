import numpy as np
from PIL import Image, ImageDraw
import sys
sys.setrecursionlimit(10**6)

def quicksort_r(array):
    if len(array) < 2:
        return array
    
    pivot = array[0]
    less = [x for x in array[1:] if x<=pivot]
    greater = [x for x in array[1:] if x>pivot]

    return quicksort_r(greater)+[pivot]+quicksort_r(less)


def reduce_rect(rect_w,rect_h, circles : list,draw):
    i = 0
    while i<len(circles):
        x = circles[i]
        if rect_h >= 2*x and rect_w >= 2*x:
            del circles[i]
            draw.ellipse((rect_w-2*x, rect_h-2*x, rect_w,rect_h), fill = 'blue', outline ='blue')
            return np.pi * x * x + reduce_rect(2*x,rect_h-2*x,circles,draw) + reduce_rect(rect_w-2*x,rect_h,circles,draw)
        i+=1
    return 0




def main():
    l = []#[2000,500,100,10,1000]
    with open('/home/fuse-power/github/dz_algo_1/algo/cpp/D:\hello.txt', 'r') as file:
        for line in file:
            try:
                l.append(int(line))
            except:
                continue
    l = quicksort_r(l)
    h, w = 5000, 5000#list(map(int,input().split()))
    s_rect = h * w
    im = Image.new('RGB', (w, h), (219, 193, 27))
    draw = ImageDraw.Draw(im)
    s_circles = reduce_rect(h,w,l,draw)
    im.save('circles.jpg', quality=95)
    print('Total area  = ', s_rect)
    print('Circled area  = ', s_circles)
    #s_circles2 = backpack_rectangle(h,w,l)
    #print('Circled area 2 = ', s_circles2)
    print(s_circles/s_rect)
if __name__ == '__main__':
    main()



def backpack_rectangle(rect_h,rect_w, circles : list):
    w = rect_h * rect_w
    n = len(circles)
    dp = [[0 for _ in range (w+1) ] for _ in range (n + 1) ]
    dp[0][0] = True
    for i in range (1, n+1):
        for j in range (w +1):
             dp[i][j] = dp[i-1][j] or (j - calc_area(circles[i-1]) >= 0 and dp[i-1][j - calc_area(circles[i-1])])
    ans = 0
    for i in range (w + 1):
        if i > ans and dp[n][i]:
            ans = i
    return ans

def calc_area(x):
    return int(round(x*x*np.pi))