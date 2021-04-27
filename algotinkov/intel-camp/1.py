A =  [14,15,14,16,13,11,12]
B = [15,15,15,14,13,12,11,11,11]
C = []
#D = [1,5,3,-100]
D = [5,4,3,2,1]
E = [3,3,3,2,2,1,1,1]
F = [6,5,4,3,2,1,7,1,4,3,0,-1]
#[] for i in range(len(A))]
class Solution: 
    def solve(self, array):
        ans = []
        i = 0
        while i < len(array):
            stop = i
            t = i
            for j in range(i+1,len(array)):
                if array[j] >= array[i]:
                    stop = j
            if stop == i:
                ans.append(i)
            i = max(stop+1,t+1)
        return ans        

#print(find(A))
# print(Solution.solve(A))
# print(Solution.solve(B))
# print(Solution.solve(C))
# print(Solution.solve(D))
# print(Solution.solve(E))
print(Solution.solve(F))
#print(find(C))