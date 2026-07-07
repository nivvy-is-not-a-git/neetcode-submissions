class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2!=0):
            return False
        
        matching_open = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        stack = []

        for character in s:
            if character == "{" or character =="[" or character=="(":
                stack.append(character)
            else:
                if len(stack)==0:
                    return False
                top_character = stack.pop()
                if (top_character!=matching_open[character]):
                    return False
        
        return len(stack)==0

                