class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = abs(len(nums)/2)
        frequency = {}
        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1
        for number in frequency:
            print (number)
            if frequency[number] >= majority:
                return number
        

            