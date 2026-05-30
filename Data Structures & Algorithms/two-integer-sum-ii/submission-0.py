class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            window_sum=numbers[i]+numbers[j]
            if window_sum>target:
                j-=1
            elif window_sum<target:
                i+=1    
            elif window_sum==target:
                return [i+1, j+1]
                
                
            
              
                
        