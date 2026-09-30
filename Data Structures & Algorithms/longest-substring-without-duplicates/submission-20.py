class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen_chars=set()
        maximum = 0

        for i in range(len(s)):
            
            while s[i] in seen_chars:
                seen_chars.remove(s[left])
                left+=1
                
            seen_chars.add(s[i])
            if (current:=i-left+1) > maximum:
                maximum = current
        return maximum
            
        

            