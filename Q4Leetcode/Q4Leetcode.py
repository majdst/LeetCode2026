class Solution:

    def twolist(self, list1: list, list2: list)->int:

        """Input: nums1 = [1,3], nums2 = [2]"""

        list_new = list1 + list2

        m = len(list_new)
        
        swap = True
        while swap: # sort the new list
            swap = False
            for num in range(m-1):

                if list_new[num] > list_new[num+1]:

                    list_new[num], list_new[num+1] = list_new[num+1], list_new[num] 
                    swap = True
        
        if m % 2 == 0:
            median = (list_new[m//2]+list_new[(m//2)-1])/2
        else:
            median = list_new[m//2]

        return median
    

mylist = Solution()
x = mylist.twolist([1,2], [3,4])
print(x)