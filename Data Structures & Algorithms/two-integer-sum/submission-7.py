class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        twonum = []
        i=0
        for num in nums:
            if (target-num) not in seen:
                seen[num] = i
            else:
                return [seen[target-num], i]
            i+=1
        
        

        
        