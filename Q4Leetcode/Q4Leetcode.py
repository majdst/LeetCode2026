"""Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

class Solution:
    def median(self, num1:list, num2:list)->int:
        # Conventional method with time Complexity of O((m+n)log(m+n))
        num = []
        num = num1 + num2 
        num.sort() #O((m+n)log(m+n))
        l = len(num)

        if l % 2 != 0:
            medi = num[l//2]
        
        else:
            medi = 0.5 * (num[l//2] + num[l//2 - 1])
        
        return medi

    def median1(self, num1:list, num2:list)->int:
        #Second method with TimeComplexity of O(m+n)
        
        def merge(x:list, y:list)->list:
            newlist = []
            r, l = 0, 0
            while r < len(x) and l < len(y):

                if x[r] < y[l]:
                    newlist.append(x[r])
                    r += 1
                
                else:
                    newlist.append(y[l])
                    l += 1
            while r < len(x):
                newlist.append(x[r])
                r += 1
            
            while l < len(y):
                newlist.append(y[l])
                l += 1
            
            return newlist
        
        list1 = merge(num1, num2)
        leng = len(list1)

        if leng % 2 != 0:
            med = list1[leng//2]
        else:
            med = (list1[leng//2] + list1[leng//2 - 1]) * 0.5
        
        return med
    
    def medianbinary(self, num1:list, num2:list)->int:
        # Binary seaech method with Time Complexity of O(log(min(m, n)))

        if len(num1) > len(num2): # Always first list should be smaller
            num1, num2 = num2, num1

        m, n = len(num1), len(num2)
        low, high = 0, m

        while low <= high:
            cut1 = (low + high)//2
            cut2 = (m+n)//2 - cut1

            left1 = float('-inf') if cut1 == 0 else num1[cut1 - 1]
            right1 = float('inf') if cut1 == m else num1[cut1]

            left2 = float('-inf') if cut2 == 0 else num2[cut2 - 1]
            right2 = float('inf') if cut2 == n else num2[cut2]

            #Final check
            if left1 > right2:
                high = cut1 - 1
            elif left2 > right1:
                low = cut1 + 1

            else:
                if (m+n)%2 != 0:
                    return min(right1, right2)
                
                else:
                    return (min(right1, right2)+max(left1, left2))/2


y = Solution()
print(y.medianbinary([1, 5, 12], [0, 2]))

