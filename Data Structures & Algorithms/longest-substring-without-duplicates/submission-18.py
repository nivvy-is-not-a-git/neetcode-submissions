class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer = 0
        seen_chars=set()
        maximum = 0
        
     

        for i in range(len(s)):
            if s[i] in seen_chars:
                while s[i] in seen_chars:
                    seen_chars.remove(s[pointer])
                    pointer+=1
            seen_chars.add(s[i])
        
            if (current:=i-pointer+1)>maximum:
                maximum = current
            
        return maximum


            