class Solution:

    #Regarding the bug i had where i didn't use stack.copy():
  ###  Python variables are pointers to objects. Changing a variable just makes it point somewhere new; the old object isn’t touched.

##Ints can’t be edited in place, so sharing their addresses is safe. Lists can be edited in place, so if two names point to the same list, changes through one show up in the other.

##That’s why combinations.append(stack) broke: I saved the address of the stack, and backtracking kept editing it. I need to save a copy.

###A shallow copy makes a new outer list but reuses the addresses inside it. That’s enough for a list of ints, since those values can never change. For a list of lists, the inner lists are still shared and can be edited, so I’d need a deep copy to duplicate every level.

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(i, target):
            if i == len(nums):
                return
            curr.append(nums[i])
            remaining = target-nums[i]
            if remaining==0:
                combinations.append(curr[:])
            elif remaining>0:
                backtrack(i, remaining)
            curr.pop()
            backtrack(i+1, target)
        curr = []
        combinations = []
        backtrack(0, target)
        return combinations
