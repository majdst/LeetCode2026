"""Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

class Solution:
    def median(self, num1:list, num2:list)->int:
        
        #Binary Search Method

        if len(num1) > len(num2):

            num1, num2 = num2, num1

        m, n = len(num1), len(num2)

        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n) //2 - cut1

            l1 = float('-inf') if cut1 == 0 else num1[cut1 - 1]
            r1 = float('inf') if cut1 == m else num1[cut1]

            l2 = float('-inf') if cut2 == 0 else num2[cut2 - 1]
            r2 = float('inf') if cut2 == n else num2[cut2]

            if l1 > r2:
                high = cut1 - 1

            elif l2 > r1:
                low = cut1 + 1
            else:
                if (m+n) % 2 != 0:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
                
    


            
           
           

y = Solution()
print(y.median([1,3], [2, 4, 5]))

