class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        for i in range(len(strs)):
            anagram={}
            for j in range(len(strs[i])):
                ch = strs[i][j]
                anagram[strs[i][j]] = anagram.get(strs[i][j], 0) + 1
            key = tuple(sorted(anagram.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(strs[i])
        return list(groups.values())

        