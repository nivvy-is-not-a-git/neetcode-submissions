class Solution:

    #Regarding the bug i had where i didn't use stack.copy():
  ###  Python variables are pointers to objects. Changing a variable just makes it point somewhere new; the old object isn’t touched.

##Ints can’t be edited in place, so sharing their addresses is safe. Lists can be edited in place, so if two names point to the same list, changes through one show up in the other.

##That’s why combinations.append(stack) broke: I saved the address of the stack, and backtracking kept editing it. I need to save a copy.

###A shallow copy makes a new outer list but reuses the addresses inside it. That’s enough for a list of ints, since those values can never change. For a list of lists, the inner lists are still shared and can be edited, so I’d need a deep copy to duplicate every level.

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