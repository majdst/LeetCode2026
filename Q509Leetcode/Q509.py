class Solution:
    def fibo(self, n:int)->int:
        #O(2^n)
        def helper(x:int):
            if x <= 1:
                return x
            
            return helper(x-1) + helper(x-2)
        
        return helper(n)
    
    def fibo1(self, n:int)->int:
        def helper(x):
            newD = {}
            if x <= 1:
                return x
            if x in newD:
                return newD[x]
            
            newD[x] = helper(x-1) + helper(x-2)
            return newD[x]
        
        return helper(n)
x = Solution()
print(x.fibo1(20))