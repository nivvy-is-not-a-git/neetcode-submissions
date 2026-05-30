class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums={}
        for i in range(len(nums)):
            sums[nums[i]]=i
        print (sums)

        for i in range(len(nums)):
            if ((target-nums[i] in sums) and i!=sums[target-nums[i]]):
                return [i, sums[target-nums[i]]]
            

        
