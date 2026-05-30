class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for num in nums:
            numbers[num] = 1 +numbers.get(num, 0)
        for number in numbers:
            if numbers[number]>1:
                return True
        return False
