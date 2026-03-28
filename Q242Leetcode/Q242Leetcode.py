class solution:

    def isAnagram(self, s: str, t: str) -> bool:
        #Not a efficient method. 
        newD = {}
        newL = []
        newL.append(s)
        newL.append(t)

        for item in newL:
            key = "".join(sorted(item))

            if key not in newD:
                newD[key] = [item]
            else:
                newD[key].append(item)
            
        return len(newD) == 1
    
x = solution()
print(x.isAnagram("anagram", "nagaram"))  
