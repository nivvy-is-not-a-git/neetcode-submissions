class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            word = str(len(strs[i])) + "#" + strs[i]
            strs[i] = word
        return "".join(strs)


    def decode(self, s: str) -> List[str]:
        point = 0
        strs=[]
        3#abc2#de
        while point<len(s):
            number=""
            while s[point]!="#":
                number+=s[point]
                point+=1
            original_point = point+1
            point+=int(number)+1
            strs.append(s[original_point:point])
        return strs
            
            
        