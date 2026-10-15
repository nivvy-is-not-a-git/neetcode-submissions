class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(target, stack, counter, combinations, nums):
            for i in range(counter, len(nums)):
                stack.append(nums[i])
                if target-nums[i] == 0:
                    stack_copy = stack.copy()
                    combinations.append(stack_copy)
                    stack.pop()
                    continue
                elif target-nums[i]>0:
                    backtrack(target-nums[i], stack, i, combinations, nums)
                    stack.pop()
                else:
                    stack.pop()
        combinations = []
        backtrack(target, [], 0, combinations, nums)

        return combinations