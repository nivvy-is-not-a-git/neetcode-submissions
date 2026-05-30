class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet={}
        anagrams={}
        finalAnagrams=[]
        anagramIndex=0
        frequency=[]
        for i in range(26):
            frequency.append(0)
        
        for i in range(len(strs)):
            for j in range (len(strs[i])):
                frequency[ord(strs[i][j])-ord('a')]+=1
            key=tuple(frequency)
            if key not in anagrams:
                anagrams[key]=[strs[i]]
            else:
                anagrams[key].append(strs[i])
            for j in range(26):
                frequency[j]=0
                
        print (anagrams)
        for key in anagrams:
            finalAnagrams.append(anagrams[key])
        return finalAnagrams
            
            
                    
