class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        length = 0
        max_length = 0
        j = 0
        for i in range(len(s)):
            while j<len(s) and s[j] not in dictionary:
                print (j, s[j])
                dictionary[s[j]] = 0
                j+=1
            
            print ("next sequence")
            dictionary.pop(s[i])
            if j-i>max_length:
                max_length= j-i
            
            
        
        return max_length