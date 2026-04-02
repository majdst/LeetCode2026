class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        #Bruteforce O(n^2) --> For big lists, it's not working
        maxS = float('-inf')
        l = len(nums)
        for i in range(l-k+1):
            trg = 0
            for j in range(i, i+k):
                trg += nums[j]

            if trg > maxS:
                maxS = trg
        return maxS/k
    
    def findMaxAverage1(self, nums: list, k: int) -> float:
        #O(n) Time Complexity 
        newS = sum(nums[:k])
        maxS = newS
        l = len(nums)

        for i in range(k, l):
            newS += nums[i] - nums[i-k]

            if newS > maxS:
                maxS = newS
        return maxS/k

     
x = Solution()
print(x.findMaxAverage1([5], 1))