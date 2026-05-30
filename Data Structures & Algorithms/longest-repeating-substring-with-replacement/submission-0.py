class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        max_length = 0
        

        hash = {}

        
        window_size = 0

        while (right<len(s)):
            print (s[left:right+1])
            print (hash)
            print (max_length)
        
            hash[s[right]] = hash.get(s[right], 0) + 1        
                
            if (right - left + 1) - max(hash.values()) > k:  
                hash[s[left]]-=1                 
                left +=1
            max_length = max(max_length, right - left +1)
            right += 1
                
                

            
            
            

            

        return max_length