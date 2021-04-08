"""
SOLVING
"""
_inf = -100000

def main():
    N, W =(int(_)for _ in  input().split())
    weigths = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    dp = [[_inf] * (W+1) for i in range(N+1)]  #number of weight is number of row - 1
    dw = [[0]* (W+1) for i in range(N+1)]
    dp[0][0] = 0
    for i in range(1,N+1):
        weight = weigths[i-1]
        cost = costs[i-1]
        for j in range(W+1):
            if (j - weight) < 0:
                dp1 = _inf
                #dp2 = False
            else:
                dp1 = dp[i-1][j-weight] + cost
                #dp2 = dp[i][j-weight]
            dp0 = dp[i-1][j]
            dp[i][j] = max(dp[i-1][j], dp1)
            if dp0 > dp1:
                dw[i][j] = 0
            else:
                dw[i][j] = 1
    #print(dp[N][W])
    maxN = dp[N][0]
    it = 0     
    for i in range(W,-1,-1):
        a =  dp[N][i]
        if dp[N][i] > maxN:
            it = i
            maxN = dp[N][i]
    ans = []
    for i in range(N, -1, -1):
        if dw[i][it] == 1:
            ans.append(i)
    print(len(ans))
    for x in ans:
        print(x, end=' ')

if __name__ == '__main__':
    main() 