class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
#BruteForce method--> problem with big number that make Time Exceed Error
        negative = (dividend < 0) != (divisor < 0) 
        #Means if one of them are negative, return True else if both neg or positive, return False

        D, d = abs(dividend), abs(divisor)

        count = 0
        while D>=d:
            D -= d
            count += 1
        
        if negative:
            count = -count

        return min(max(count, -2**31), 2**31-1)
    # this one line is instead of if, elif, and else

x = Solution()
print(x.divide(25, -2))