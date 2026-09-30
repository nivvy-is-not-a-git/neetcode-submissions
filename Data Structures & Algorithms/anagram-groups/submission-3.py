class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for i in range(len(strs)):
            anagram = {}
            for j in range(len(strs[i])):
                anagram[strs[i][j]] = anagram.get(strs[i][j], 0) + 1
            anagram = tuple(sorted(anagram.items()))
            if anagram in groups:
                groups[anagram].append(strs[i])
            elif anagram not in groups:
                groups[anagram] = []
                groups[anagram].append(strs[i])
        return list(groups.values())
                
        