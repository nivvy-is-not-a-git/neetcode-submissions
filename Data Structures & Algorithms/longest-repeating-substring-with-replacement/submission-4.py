class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequency = {}
        maximum_window = 0
        
        maximum = 0


        for i in range(len(s)):
            frequency[s[i]] = frequency.get(s[i], 0) + 1
            for key in frequency:
                if frequency[key]>maximum:
                    maximum = frequency[key]
            # print ("\n")
            # for j in range(left, i):
            # #     print (s[j], end = "")
            # print ("Window length: ", window:= i - left + 1, "  Maximum: ", maximum)
            while (window:= i - left + 1) - maximum > k:
                # print ("triggered")
                frequency[s[left]] -= 1
                left +=1
                # print (left)
                
            if window>maximum_window:
                maximum_window = window
        return maximum_window
        
        
        
        
        


