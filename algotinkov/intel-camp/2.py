#[] for i in range(len(A))]
class Solution: 
    @staticmethod 
    def MaxPooling(a: list, k: int) -> list: 
        b = []
        for i in range(len(a[:k])):
            t = a[i:i+k]
            b.append((a[i], max(t)))
        ans = [b[0][1]]
        #ans.append(max(a[:k]))
        #m = ans[0]
        for i in range(k,len(a)):
            del b[0]
            b.append((a[i],max(a[i],b[0][1])))            
            ans.append(b[0][1])
            # if a[i]>m:
            #     ans.append(a[i])
            #     m = a[i]
            # else:
            #     ans.append(m)
        return ans
#print(find(A))
# print(Solution.solve(A))
# print(Solution.solve(B))
# print(Solution.solve(C))
# print(Solution.solve(D))
# print(Solution.solve(E))
print(Solution.MaxPooling([2, 7, 3, 1, 5, 2, 6, 2],4))
#print(Solution.MaxPooling([2, 1, 5],1))
#print(Solution.MaxPooling([2, 1, 5],3))
#print(find(C))