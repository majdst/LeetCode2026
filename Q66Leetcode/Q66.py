class Solution:
    def plusOne(self, digits: list):
        l = len(digits)
        num = 0
        for i in digits:
            num = num * 10 + i
        num += 1
        
        newL = []
        while num > 0:
            res = num % 10
            newL.append(res)
            num = num // 10  # update num each iteration
        
        newL.reverse()  # digits were added backwards
        return newL

x = Solution()
print(x.plusOne([4,3,2,1]))