class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers={}
        for index, number in enumerate (nums):
            print (target-number)
            if ((target-number) in numbers):
                return [numbers[target-number],index]
            else:
                numbers[number]=index
        
