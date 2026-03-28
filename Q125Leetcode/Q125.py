class Solution:
    def isPalindrome(self, s:str)->bool:

        newWord = "".join([char for char in s if char.isalnum()]).lower()

        return newWord == newWord[::-1]
    
x = Solution()
print(x.isPalindrome("race a car"))