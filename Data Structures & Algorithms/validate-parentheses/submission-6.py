class Solution:
    def isValid(self, s: str) -> bool:
        top = -1
        opening={'(':1, '{':2, '[':3}
        closing={')':1, '}':2, ']':3}
        stack=[]
        if len(s)==1:
            return False
        for i, letter in enumerate(s):
            print (f"iteration {i}")
            if letter in opening:
                stack.append(letter)
                top+=1
            else:
                if top<0:
                    return False
                if opening[stack[top]] == closing[letter]:
                    stack.pop()
                    top-=1
                else:
                    return False
        return top==-1
            

