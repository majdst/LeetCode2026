class Dictionary:
    def dicnew(self, s:str)->dict:

        newD = {}
        for item in s:
            newD[item] = newD.get(item, 0) + 1

        return newD
    
    def quest2(self, s:list, target:int):
        
        newD = {}
        l = len(s)
        
        for item in range(l):

            trg = target - s[item]
            if trg in newD:
                return (newD[trg], item)

            newD[s[item]] = item 
    def quest3(self, s:str)->str:
        #"leetcode"
        newD = {}
        for item in s:
            newD[item] = newD.get(item, 0) + 1
        for i in s:
            if newD[i] == 1:
                return i
    def quest4(self, s:list):

        newD = {}
        for item in s:
            key = "".join(sorted(item))

            if key not in newD:
                newD[key] = [item]
            else:
                newD[key].append(item)
        
        return newD.values()
    
    def quest5(self, s:list)->bool:
        #"anagram", "nagaram"
        newD = {}

        for item in s:
            key = "".join(sorted(item))

            if key not in newD:
                newD[key] = [item]
            else:
                newD[key].append(item)
            
        return len(newD) == 1
    
x = Dictionary()
print(x.dicnew('abcabccbaqwqd'))
print(x.quest2([2,4,7, 11, 21], 32))
print(x.quest3('leetcode'))
print(x.quest4(["eat","tea","tan","ate","nat","bat"]))
print(x.quest5(["anagram", "nagaram"]))