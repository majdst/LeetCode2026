class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        newD = {}
        newD1 = {}
        for s1, t1 in zip(s, t):
            if s1 in newD:
                if newD[s1] != t1:
                    return False
            else:
                newD[s1] = t1 
            
            if t1 in newD1:
                if newD1[t1] != s1:
                    return False
            else:
                newD1[t1] = s1
        
        return True
x = Solution()
print(x.isIsomorphic("egg", "add"))