"""
SOLVING
"""
inf = 100000

def main():
    N =int(input())
    a = list(map(int, input().split()))
    dp = [inf] * (N-1)
    dp.insert(0,-1)
    r = dp.copy()
    p = dp.copy()
    for i in range(N):
        for j in range(N):
            if dp[j] < a[i] and dp[j+1] > a[i]:
                dp[j+1] = a[i]
                r[j+1] = i
                p[i] = r[j]
    print(1)  
if __name__ == '__main__':
    main() 