A = [-1,2,1]
B = [2,-1]
C = [1,2]
#D = [1,5,3,-100]
D = [1,5,3,-1000,-100,50,-100,100]
#[] for i in range(len(A))]
class Solution: 
    @staticmethod 
    def solve(a: list) -> int:  
        dp = [0] * len(a)
        l = len(a)
        for i in range(l):
            if i < 2:
                dp[i] += a[i]
            else:
                dp[i] += max(dp[i-1], dp[i-2]) + a[i]
        return dp[l-1]

#print(find(A))
print(Solution.solve(A))
#print(find(C))