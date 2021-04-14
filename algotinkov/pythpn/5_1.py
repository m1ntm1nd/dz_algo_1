"""
SOLVING
"""
def func(N,A):
    for i in range(N,0,-1):
        if A[i]>A[i-1]:
            t = A[i-1]
            for j in range(N,i-1,-1):
                if A[j]>t:
                    A[i-1], A[j] = A[j], t
                    return A[:i] + A[N:i-1:-1]
            break
    else:
        return A[::-1]
            
def print_list(A):
    for x in A:
        print(x, end=' ')
    #print('\n')

def print_file(name, t):
    w = open(name, "a")
    for x in t:
        p = str(x) + ' '
        w.write(p)
    w.write('\n')
    w.close()

def main():
    f = open('nextperm.in', "r")
    
    num = 0
    for ln in f:
        if num % 2 == 0:
            N = int(ln)
        else:
            A = list(map(int,ln.split()))
            t = func(N-1,A)
            print_file('nextperm.out', t)
        num += 1
    f.close()


if __name__ == '__main__':
    main() 