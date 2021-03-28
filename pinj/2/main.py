def fib(n):
    f = []
    f.append(1)
    f.append(1)
    for x in range(2,n):
        f.append(f[x-1] + f[x-2])
    return f[n-1]

def three_ones(n):
    dp = [0,0,0,1]
    s = 1
    if n==1:
        return 2
    elif n==2:
        return 4
    for i in range(4,n+1):
        dp.append(dp[i-1]*2)
        s+=dp[i-1]*2
    return 2**n - dp[n] - dp[n-1]


def main():
    N = int(input())
    #a = list(map(int, input().split()))
    print(three_ones(N))
    #print(three_ones(5))


if __name__ == '__main__':
    main()