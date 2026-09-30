class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        right = False #this bool tracks where the drop happens, e.g. drop from [3, 4, -> 1, 2]. knowing where the drop happens, we can tell what side target is on. for instance if we know the drop is on the right, and target is less than hi, than we know that target is on the right. 
        while lo<=hi:
            mid = (hi+lo)//2
            m = nums[mid]
            l = nums[lo]
            h = nums[hi]
                #the issue now is that we dont know whether to go right or left since we dont know wheter the drop happens on the right or the left of mid. as a result, we may need to first determine the side that has the lower portion . the issue is a test case like [3, 1, 2]. how do we know which way to go to get target? 
            if m == target:
                return mid
            elif m>=h and target<=h:  #[3, 4, 5, 1, 2] target = 1. this should gradually become l = 1. 
                lo = mid + 1
            
                
            elif m>=h and target>h and target<m:  #[2, 3, 4, 5, 1] target = 3 , we want the logic to look on the left side for the target
                hi = mid-1
            
            elif m>=h and target>h and target>m:   #[2, 3, 4, 5, 1] target = 5, we want the logic to look on the right side for the target
                lo = mid+1

            elif m<h and target>h:      #[5, 6, 1, 2, 3, 4] target = 5 , we want the logic to look on the left side for the target
                hi = mid-1
            elif m<h and target<=h and target>m:  #[5, 6, 1, 2, 3, 4] target = 3 , 
                lo = mid+1
            elif m<h and target<=h and target<m: #[6, 7, 1, 2, 3, 4, 5] target =1
                hi = mid-1
        return -1

        

