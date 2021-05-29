
def hash(s,ppower):
    M = 10**9 + 7
    res = 0
    for i in range(len(s)):
        res = (res + (ord(s[i])-ord('a')+1) * ppower[i]) % M
    return res % M

def hashed(s,ppower):
    M = 10**9 + 7
    res = 0
    hashed = []
    for i in range(len(s)):
        res = (res + (ord(s[i])-ord('a')+1) * ppower[i]) % M
        hashed.append(res)
    return hashed

def print_list(A):
    for x in A:
        print(x, end=' ')

def main():
    M = 10**9 + 7
    P = 31
    s = input() 
    t = input()
    ppower = [(P ** i % M) for i in range(len(s)+1)]
    smallhash = hash(t,ppower)
    hshed = hashed(s,ppower)
    hshed.insert(0,0)
    ans = []
    for i in range(len(s)-len(t)+1):
        j = i + len(t)
        bighash = (hshed[j] - hshed[i]* ppower[i]) % M  % M
        if (bighash == (smallhash* ppower[i]%M)):
            ans.append(i)
    print_list(ans)





if __name__ == "__main__":
    main()
