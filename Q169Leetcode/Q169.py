class Solution:
    def majorityElement(self, nums: list) -> int:
#Brutforce Method Time Complexity of O(n^2)
        newD = {}
        for i in nums:
            newD[i] = newD.get(i, 0) + 1

        maxL, ans = 0, 0

        for item in newD:
            if newD[item] > maxL:
                maxL = newD[item]
                ans = item
        return ans


x = Solution()
print(x.majorityElement([3,2,3]))