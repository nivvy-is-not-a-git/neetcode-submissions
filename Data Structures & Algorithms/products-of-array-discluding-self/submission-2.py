class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        prefix_product = 1
        for i in range(length):
            result[i] = prefix_product
            prefix_product *=nums[i]
        suffix_product = 1
        for j in range(length-1, -1, -1):
            print(j)
            result[j]*= suffix_product
            suffix_product *= nums[j]

        return result