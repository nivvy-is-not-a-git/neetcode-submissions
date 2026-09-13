class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_count = 0
        for i in range(1,len(strs)):
            if len(strs[i])<len(strs[min_count]):
                min_count = i
        start_string = strs[min_count]
        for i in range(len(strs)):
            if i==min_count:
                continue
            for j in range(len(start_string)):
                if strs[i][j]!=start_string[j]:
                    start_string = start_string[0:j]
                    break
        return start_string
                    
        

        
        