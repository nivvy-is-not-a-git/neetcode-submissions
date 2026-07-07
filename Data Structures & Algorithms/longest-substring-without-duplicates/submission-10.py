class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left = 0
        right = 0
        best_length = 0

        for right in range(len(s)):
            current_char = s[right]
            while current_char in seen_chars:
                seen_chars.remove(s[left])
                left+=1
            seen_chars.add(current_char)
            window_length = right - left + 1

            if window_length>best_length:
                best_length = window_length

        return best_length


            