class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        best_area=-1
        while i<j:
            area= min(heights[i], heights[j])*(j-i)
            if area>best_area:
                best_area=area
            if heights[j]<heights[i]:
                j-=1
            elif heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            
        return best_area



