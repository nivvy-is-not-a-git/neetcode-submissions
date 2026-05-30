class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers={}
        for index, number in enumerate (nums):
            print (target-number)
            if ((target-number) in numbers):
                if (index<numbers[target-number]):
                    i=index
                    j=numbers[target-number]
                else:
                    i=numbers[target-number]
                    j=index
                return [i,j]
            else:
                numbers[number]=index
        
