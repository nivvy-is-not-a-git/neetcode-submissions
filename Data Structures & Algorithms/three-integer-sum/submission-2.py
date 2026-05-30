class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets=[]
        windows=set()
        
        for i in range (len(nums)-2):
            j=i+1
            k=len(nums)-1
            target=-nums[i]
            while j<k:
                window=(nums[i],nums[j], nums[k])
                window_sum=nums[j]+nums[k]
                if window_sum<target:
                    j+=1
                elif window_sum>target:
                    k-=1
                elif window_sum==target and window not in windows:
                    windows.add(window)
                    print (window)
                    triplets.append(window)
                    j+=1
                    k-=1
                else:
                    j+=1
                    k-=1    


                
            
            
        return triplets
        

