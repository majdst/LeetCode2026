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

    def majorityElement1(self, nums: list) -> int:
#efficient and Time Complexity if O(n)
        candidate = 0
        maxL = 0

        for item in nums:

            if maxL == 0:
                candidate = item
            
            if item == candidate:
                maxL += 1
            
            if item != candidate:
                maxL -= 1
        
        return candidate

x = Solution()
#print(x.majorityElement([3,2,3]))
print(x.majorityElement1([3,2,3]))