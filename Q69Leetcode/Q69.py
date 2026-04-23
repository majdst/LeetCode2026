import numpy as np
class Solution:
    def mySqrt(self, x: int) -> int:
        m = np.sqrt(x)
        return int(m)
    
x = Solution()
print(x.mySqrt(8))