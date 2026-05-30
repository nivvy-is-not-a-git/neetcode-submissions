class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictionary = {}
        length = len(s1)

        s1_hash = {}
        left = 0
        right = 0
        for i in range(len(s1)):
            s1_hash[s1[i]] = s1_hash.get(s1[i], 0) + 1

        
        while right<len(s2):
            
            dictionary[s2[right]] = dictionary.get(s2[right], 0) + 1
            right +=1
            
            
            if right-left > len(s1):
                dictionary[s2[left]] -= 1
                if (dictionary[s2[left]] ==0):
                    del(dictionary[s2[left]])
                left+=1
                

            

            if s1_hash == dictionary:
                return True

            
            
            
                    
                
        return False
