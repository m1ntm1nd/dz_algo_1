"""
SOLVING
"""
a = [0] * 10000

def f(x):
    if a[x]:
        return a[x]
    if x < 2: 
        return x
    else:
        a[x] = f(x-1) + f(x-2)
    return a[x]

def main():
    M = 10**9 + 7
    s = input()
    if s.count('m'):
        print(0)
    else:
        ans = 1
        podstrs = []
        i = 0
        while i<len(s):
            if s[i] == 'u':
                podstr = 1
                i = i + 1
                while (i<len(s)) and s[i] == 'u':
                    podstr += 1
                    i = i + 1
                podstrs.append(podstr)
            elif s[i] == 'n':
                podstr = 0
                while (i<len(s)) and s[i] == 'n':
                    podstr += 1
                    i += 1
                podstrs.append(podstr)
            i+=1
        for x in podstrs:
            ans *= f(x+1) % M
        print(ans)
if __name__ == '__main__':
    main()