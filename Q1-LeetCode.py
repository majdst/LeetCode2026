class Solution:
    def twoSum(self, nums:list[int], target: int)->list[int]:


       m = len(nums)
       s = {}

       for i in range(m):

           rem = target - nums[i]

           if rem in s:

               return [s[rem], i]

           s[nums[i]] = i            
        



numx = [2, 11, 15, 5,  7]
targ = 9
solution = Solution()
print(solution.twoSum(numx, targ))