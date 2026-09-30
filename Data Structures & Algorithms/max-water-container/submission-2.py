class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights)-1
        while left<right and right<len(heights):
            
            if (area:=min(heights[right], heights[left])* (right-left))>max_water:
                max_water = area
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
            
        return max_water


            

