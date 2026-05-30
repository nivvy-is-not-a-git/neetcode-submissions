class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        t_freq={}
        for i, character in enumerate (s):
            if character not in s_freq:
                s_freq[f'{character}']=0
            s_freq[f'{character}']+=1
        for i, character in enumerate (t):
            if character not in t_freq:
                t_freq[f'{character}']=0
            t_freq[f'{character}']+=1
        if s_freq==t_freq:
            return True
        else:
            return False