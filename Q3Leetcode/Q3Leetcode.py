class Solution:

    def lofLong(self, s:str) -> int:
        
        def helperfunc(string:str):
            seen = set()

            for char in string:

                if char in seen:

                    return False
            
                seen.add(char)

            return True
        
        
        max_l = 0
        n = len(s)

        for i in range(n):

            for j in range(i+1, n+1):

                y = s[i:j]

                if helperfunc(y):

                    max_l = max(max_l, j-i)

        return max_l
    

mylist = Solution()
x1 = mylist.lofLong("abcabcbpoqwe")

print(x1)