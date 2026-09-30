class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagrams = set()
        s_anagram = {}
        t_anagram = {}
        for i in range(len(s)):
            s_anagram[s[i]] = s_anagram.get(s[i], 0) + 1
        for i in range(len(t)):
            t_anagram[t[i]] = t_anagram.get(t[i], 0) + 1
        s_anagram = tuple(sorted(s_anagram.items()))
        t_anagram = tuple(sorted(t_anagram.items()))

        anagrams.add(s_anagram)

        if t_anagram in anagrams:
            return True
        else:
            return False

            