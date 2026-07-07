class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26


        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            s2_index = ord(s2[i]) - ord("a")
            s1_count[s1_index] +=1
            window_count[s2_index] +=1

        if s1_count == window_count:
            return True
        
        left = 0

        for right in range(len(s1),len(s2)):
            add_index=ord(s2[right]) - ord("a")
            remove_index =ord(s2[left]) - ord("a")

            window_count[add_index] +=1
            window_count[remove_index] -= 1

            left += 1

            if s1_count == window_count:
                return True
        return False