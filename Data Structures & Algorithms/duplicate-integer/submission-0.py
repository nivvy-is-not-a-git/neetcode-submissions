class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integers=[]
        for i, num in enumerate (nums):
            if num in integers:
                return True
            else:
                integers.append(num)
        return False
            