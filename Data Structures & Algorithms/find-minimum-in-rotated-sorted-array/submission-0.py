class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo<hi:
            mid = (hi+lo)//2
            h = nums[hi]
            l = nums[lo]
            m = nums[mid]
            if m >= h:
        # if mid is > h, that means the drop is in the right portion
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
        # if mid is < h, that means, ALWAYS, the lowest is in the left portion or is equal to mid. 


        #going one step deeper, looking at test case 1, m is initiall 4, and then since 4>1, lo = 3, h =4. now in the second loop, mid = 3. therefore mid = lo. since 5>1, l = 1. we stop here. and since by the end, in the smallest portion, it should be sorted, so the left is the minium, therefore we return lo. 


       #1 [2, 3, 4, 5, 1]

        # [3, 4, 5, 1, 2]

        # [5, 1, 2, 3, 4]