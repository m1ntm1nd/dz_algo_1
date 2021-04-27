A = [2,2,2,0,1,0,1,1,0]
B = [0]
C = []
#D = [1,5,3,-100]
D = [1,1,1,1,1]
E = [0,0,0,0]
E1 = [2,2,2]
E2 = [0,1,1]
E3 = [1,1,0,0]
#[] for i in range(len(A))]
class Solution(object):
    def sortExperiments(self, nums: List[int]) -> None: 
        zeros = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
        for i in range(len(nums)):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
            elif ones != 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
        return nums

#print(find(A))
#a = Solution().sortExperiments(A)
print(a)
# Solution.sortExperiments(B)
# Solution.sortExperiments(C)
# Solution.sortExperiments(D)
# Solution.sortExperiments(E)
# Solution.sortExperiments(E1)
# Solution.sortExperiments(E2)
# Solution.sortExperiments(E3)
#print(find(C))