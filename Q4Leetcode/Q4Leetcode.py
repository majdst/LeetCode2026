class Solution:

    def twolist(self, list1: list, list2: list)->int:

        merge_list = list1+list2

        merge_list.sort()


        m = len(merge_list)

        if m%2 == 0:

            median = (merge_list[m//2] + merge_list[m//2 - 1])/2

        else:
            median = merge_list[m//2]

        return median
    

mylist = Solution()
x = mylist.twolist([1,2], [3,4])
print(x)