class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        prefix = [1]
        suffix = [1]*len(nums)
        suffix[len(nums)-1] = 1

        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            product = prefix[i] * suffix[i]
            output.append(product)
        return output

        