class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        print(word)

        #Check the length
        if len(pattern) != len(word):
            return False
        
        patternToWord, wordToPattern = {}, {}

        #This is new for me: April 6
        for p, c in zip(pattern, word):
            if p in patternToWord:
                if patternToWord[p] != c:
                    return False
            else:
                patternToWord[p] = c
            
            if c in wordToPattern:
                if wordToPattern[c] != p:
                    return False
            else:
                wordToPattern[c] = p
        
        return True
    
    def wordPattern1(self, pattern: str, s: str) -> bool:
        word = s.split()
        
        return len(set(zip(pattern, word))) == len(set(pattern)) == len(set(word)) == len(pattern) == len(word)


x = Solution()
print(x.wordPattern("abba", "fish  dog dog fish"))