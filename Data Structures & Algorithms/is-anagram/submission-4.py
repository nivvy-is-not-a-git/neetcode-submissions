class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freq={}
        t_freq={}
        for index, character in enumerate (s):
            if character not in s_freq:
                s_freq[f'{character}']=0
            else:
                s_freq[f'{character}']+=1
        for index, character in enumerate (t):
            if character not in t_freq:
                t_freq[f'{character}']=0
            else:
                t_freq[f'{character}']+=1
        
        if s_freq==t_freq:
            return True
        else: 
            return False