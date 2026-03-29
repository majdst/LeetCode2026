class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
#Bruteforce Method
        newD = {}
        for i in nums:
            newD[i] = newD.get(i, 0) + 1 
        
        for i in nums:
            if newD[i] >1:
                return True
            
        return False
        
x = Solution()
print(x.containsDuplicate([2,14,18,22,22]))
