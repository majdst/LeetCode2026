class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        
        l = len(nums)
        k = 0

        for i in range(l):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        print(nums[:k])

x=Solution()
x.removeElement([0,1,2,2,3,0,4,2], 2)