class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}

        for num in nums:
            numbers[num] = 0
       
        length = 1
        max_length = 0
        for i in range(len(nums)):
            if (nums[i]-1 not in numbers):
                while (nums[i]+length in numbers):
                    length+=1
                    
                if length>max_length:
                    max_length = length
                length = 1
        return max_length
            
            

        