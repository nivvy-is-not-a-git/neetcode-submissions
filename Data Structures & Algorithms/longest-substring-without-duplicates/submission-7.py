class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        length = 0
        max_length = 0
        for i in range(len(s)):
            j=i
            while j<len(s) and s[j] not in dictionary:
                print (j, s[j])
                length+=1
                dictionary[s[j]] = 0
                j+=1
            
            print ("next sequence")
            dictionary = {}
            if length>max_length:
                max_length= length
            length = 0
            
            
        
        return max_length