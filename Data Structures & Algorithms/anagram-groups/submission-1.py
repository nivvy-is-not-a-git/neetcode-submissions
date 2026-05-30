class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        
        groups = []
        for string in strs:
            anagram=tuple(string)
            anagram = tuple(sorted(anagram))
            if (anagram not in dictionary):
                dictionary[anagram] = [string]
            else:
                dictionary[anagram].append(string)
        for group in dictionary:
            groups.append(dictionary[group])
        return groups
