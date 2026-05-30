class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        print (s)
        for i in range (len(s)):
            if s[-1-i]!=s[i]:
                return  False
        return True
            

        