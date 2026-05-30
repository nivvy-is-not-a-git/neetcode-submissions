class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freq={}
        t_freq={}
        for index in range (len(max(s, t))):
            if index<len(s):
                if s[index] not in s_freq:
                    s_freq[f'{s[index]}']=1
                   
                else:
                    s_freq[f'{s[index]}']+=1
            if index<len(t):
                if t[index] not in t_freq:
                    t_freq[f'{t[index]}']=1
                   
                else:
                    t_freq[f'{t[index]}']+=1

        if s_freq==t_freq:
            return True
        else: 
            return False