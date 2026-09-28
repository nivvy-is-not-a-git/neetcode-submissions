class Solution:
    def key_exists(self, frequency_t: dict, frequency_s: dict) -> bool:
        exists = True
        for key in frequency_t:
            if (frequency_s.get(key, 0))<frequency_t[key]:
                exists = False
                break
        return exists
    def minWindow(self, s: str, t: str) -> str:
        frequency_t = {}
        frequency_s = {}
        min_length = -1
        left = 0
        min_left = 0
        
        for i in range(len(t)):
            frequency_t[t[i]] = frequency_t.get(t[i], 0) + 1
        for i in range(len(s)):
        

            if s[i] in frequency_t:
                frequency_s[s[i]] = frequency_s.get(s[i], 0) + 1

                
            while (self.key_exists(frequency_t, frequency_s)):
                if (length:=i-left+1) < min_length or min_length == -1:
                    min_length = length
                    min_left = left
                if s[left] in frequency_s:
                    frequency_s[s[left]]-=1
                left +=1
                
                    
                

                    
        if min_length ==-1:
            return ""
        return s[min_left:min_left+min_length]