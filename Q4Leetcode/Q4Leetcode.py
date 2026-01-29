"""Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

class Solution:
    def median(self, num1:list, num2:list)->int:
        newlist = []
        right = 0
        left = 0

        while right < len(num1) and left < len(num2):

            if num1[right] < num2[left]:

                newlist.append(num1[right])
                right += 1
            else:
                newlist.append(num2[left])
                left += 1

        while right < len(num1):
            newlist.append(num1[right])
            right += 1

        while left < len(num2):
            newlist.append(num2[left])
            left += 1

        m = len(newlist)
        if m %2 == 0:

            median = (newlist[m//2 - 1] + newlist[m//2])*0.5

        else:
            median = (newlist[m//2])
        
        return median
    


            
           
           

y = Solution()
print(y.median([1,3], [2, 4, 5]))

