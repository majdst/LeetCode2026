class solution:

    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
    
    
x = solution()
print(x.isAnagram("sfgram", "nagaram"))  
