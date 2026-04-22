class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        newD = {}
        newL = []

        for i in nums1:
            newD[i] = newD.get(i, 0) + 1

        for j in nums2:
            if j in newD and newD[j] > 0:
                newL.append(j)
                newD[j] -= 1
        return newL        
x = Solution()
print(x.intersect([4,9,5], [9,4,9,8,4]))