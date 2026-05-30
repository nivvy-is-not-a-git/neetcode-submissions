class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sstring = {}
        tstring = {}
        for letter in s:
            
            sstring[letter] = sstring.get(letter, 0) + 1

        for letter in t:
            tstring[letter] = tstring.get(letter, 0) + 1

        for letter in s:
            if letter in tstring:
                print (letter, "found")
                tstring[letter]-=1
                if tstring[letter]==0:
                    print (letter, "popped out because empty now")
                    tstring.pop(letter)
            else:
                return False
        if len(list(tstring.keys())) != 0 :
            return False
        return True
            