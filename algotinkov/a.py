 
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]

N = int(input())
a = list(map(int, input().split()))

sel_sort(a)
for x in a:
    print(x, sep=' ',end=' ')