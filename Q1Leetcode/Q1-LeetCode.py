class Solution:
    def twoSum1(self, nums:list[int], target: int)->list[int]:

        # Brut-Force Method --> Time Complexity O(n^2)
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1, l):

                if nums[i] + nums[j] == target:
                    return [i,j]
    
    def twoSum2(self, nums:list[int], target: int)->list[int]:

        #Dictionary Method --> Time Complexity O(n)
        l = len(nums)

        newL = {}

        for i in range(l):

            trg = target - nums[i]

            if trg in newL:
                return [newL[trg], i]
            
            newL[nums[i]] = i



numx = [2, 11, 15, 5,  7]
targ = 9
solution = Solution()
print(solution.twoSum2(numx, targ))