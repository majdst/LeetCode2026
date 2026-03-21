class Solution:
    def searchAlgorithm(self, num1: list, target:int)->int:

        low, high = 0, len(num1)-1

        while low <= high:
            
            mid = (low+high)//2

            if num1[mid] == target:
                return mid
            elif num1[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1 #Not found
            

x= Solution()
y = x.searchAlgorithm([1,3,5,7,9], 7)
print(y)