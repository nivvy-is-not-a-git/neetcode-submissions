class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_count = 0
        best_length = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char not in counts:
                counts[current_char] = 0

            counts[current_char]+=1

            if counts[current_char]>max_count:
                max_count = counts[current_char]
            
            while (right - left + 1) - max_count >k:
                left_char = s[left]
                counts[left_char] -=1
                left+=1
            window_length = right - left +1

            if window_length > best_length:
                best_length = window_length
        return best_length
