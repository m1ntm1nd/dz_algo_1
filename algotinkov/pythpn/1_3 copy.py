def find_max(ans,k, max, idmax,s):
    for i in range(len(ans)):
        if ans[i]>max:
            max = ans[i]
            idmax = i
    m = max
    try:
        s[idmax+1] = s[idmax]
        for i in range(1, len(s)):
            if s[i] == s[-1]:
                ans[i][0] = ans[i-1][0] + 1
        m = find_max(ans,k-1, max, idmax,s)
    except

def main():
    n, k = list ( map ( int , input () . split () ) )
    s = list(input())
    ans = [[1,s[i]] for i in range(len(s))]
    for i in range(1, n):
        if k == 0:
            if s[i] == s[-1]:
                ans[i][0] = ans[i-1][0] + 1
        
    #while k > 0 or max(ans) != len(s):

    print(max(ans))

if __name__ == '__main__':
    main()