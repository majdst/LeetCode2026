class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:

        maxSum = float("-inf")
        l = len(nums)
        for i in range(l-k+1):
            trg = 0
            for j in range(i, i+k):
                trg += nums[j]
            
            if trg > maxSum:
                maxSum = trg
        return maxSum/k
x = Solution()
print(x.findMaxAverage([1,12,-5,-6,50,3], 4))