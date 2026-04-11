class solution:

    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
    
    def isAnagram1(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        newD = {}

        for char in s:
            newD[char] = newD.get(char, 0) + 1

        for char in t:
            newD[char] = newD.get(char, 0) - 1

            if newD[char] < -1:
                return False
        
        return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) == t.count(i):
                continue
            else:
                return False
        
        return True

x = solution()
print(x.isAnagram1("a", "ab"))  
