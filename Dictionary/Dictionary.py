class Dictionary:
    def checking(self, s:str)->dict:

        newD = {}
        
        for item in s:
            newD[item] = newD.get(item, 0) + 1

        return newD
    
    def istargetIn(self, s:str, target:int)->int:

        l = len(s)
        newD = {}
        for item in range(l):
            
            trg = target - s[item]
            if trg in newD:
                return (newD[trg], item)
            
            newD[s[item]] = item
    
    def firstSingleWord(self, s:str)->str:
        newD = {}
        for item in s:
            newD[item] = newD.get(item, 0) + 1
        
        for item in s:
            if newD[item] == 1:
                return item 
    
    def dicList(self, s:list):

        newD = {}
        for item in s:
            key = "".join(sorted(item))

            if key not in newD:
                newD[key] = [item]
            else:
                newD[key].append(item)
            
        return list(newD.values())
    
    def dinagram(self, s:list):
        newD = {}
        for item in s:
            key = "".join(sorted(item))

            if key not in newD:
                newD[key] = [item]
            else:
                newD[key].append(item)
            
        return len(newD) == 1
    
        
        
x = Dictionary()
print(x.checking("aabbccmfghghagbc"))
print("*************")
print(x.istargetIn([2,7,11,15], 9))
print("*************")
print(x.firstSingleWord("eeetmcode"))
print("*************")
print(x.dicList(["tea", "eat", "tan", "ate", "nat", "bat"]))
print("*************")
print(x.dinagram(["anagram", "nagaram"]))