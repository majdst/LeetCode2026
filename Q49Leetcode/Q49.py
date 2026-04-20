class Solution:
    def groupAnagrams(self, strs) -> list:

        newD = {}
        for i in strs:

            key = str(sorted(i))

            if key in newD:
                newD[key].append(i)

            else:
                newD[key] = [i]
        
        return list(newD.values())

x = Solution()

print(x.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))