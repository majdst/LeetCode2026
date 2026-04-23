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
    
    def plusOne1(self, digits: list):
        l = len(digits)

        for i in range(l-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[0]
        return [1] + digits

x = Solution()
print(x.plusOne1([4,3,2,1]))