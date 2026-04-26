class Solution:
    def fibo(self, n:int)->int:

        def helper(x:int):
            if x <= 1:
                return x
            
            return helper(x-1) + helper(x-2)
        
        return helper(n)
    
x = Solution()
print(x.fibo(20))