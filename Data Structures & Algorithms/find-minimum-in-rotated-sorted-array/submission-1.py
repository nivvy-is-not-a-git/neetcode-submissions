class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo<hi:
            mid = (hi+lo)//2
            l = nums[lo]
            h = nums[hi]
            m = nums[mid]
            
            print (m)
            if m>h:
                lo = mid+1
                print ("lo: ", nums[lo], "hi: ", nums[hi])
            elif m<=h:
                hi = mid
                print ("hi: ", nums[hi], "lo: ", nums[lo])
        return nums[lo]
        


        # [1, 2, 3, 4, 5, 6]
        # [6, 5, 4, 3, 2, 1]
        # [4, 5, 6, 1, 2, 3]
        # [5, 6, 1, 2, 3, 4]
        



        #binary search is logn and fixates on either recursive left or right portion . what do we know about the minimum? it is increasing from its right and there is a sudden drop from its left