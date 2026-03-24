class Solution:

    def linearSearch(self, s:list, trg:int)->int:
        #LinearSearch with TimeComplexity of O(n)

        l = len(s)

        for i in range(l):
            if s[i] == trg:
                return i
            
        return -1
    
    def binarySearch(self, s:list, trg:int)->int:
        # Binary Search with TimeComplexity of O(log(n))
        low, mid = 0, 0
        high = len(s) - 1

        while low <= high:
            mid = (low + high) // 2

            if s[mid] > trg:
                high = mid - 1

            elif s[mid] < trg:
                low = mid + 1

            else:
                return mid
        return -1
    
x = Solution()
print(x.binarySearch([2,4,7,10, 11, 32, 45, 87], 45))
print(x.linearSearch([2,4,7,10, 11, 32, 45, 87], 45))