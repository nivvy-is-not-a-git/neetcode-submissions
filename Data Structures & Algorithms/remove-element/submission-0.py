class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        notval=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                k+=1
                notval.append(nums[i])

        for i in range(k):
            nums[i]=notval[i]
        return k