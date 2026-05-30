class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = {}
        groups = set()
        for i in range(len(nums)):
            numbers[nums[i]] = numbers.get(nums[i], 0) + 1
        nums1= sorted(nums)
        print (nums1)
        check = set()
        
        for i in range(len(nums1)):
            
            for j in range(i+1, len(nums1)):
                
                complement = -nums1[i]-nums1[j]
                
                if complement in numbers and numbers[nums1[i]] > 0 and numbers[nums1[j]] > 0 and numbers[complement] > 0:
                    print (nums1[i], nums1[j], numbers[nums1[j]], complement, numbers[complement])
                    

                    if complement==nums1[i] and complement == nums1[j] and numbers[complement]<3:
                        continue

                    if (numbers[nums1[i]]==1 and complement==nums1[i]) or (numbers[nums1[j]]==1 and complement == nums1[j]):
                        continue
                    

                    triple = tuple(sorted((nums1[i], nums1[j], -nums1[i]-nums1[j])))
                    if triple in check:
                        continue
                    else:
                        check.add(triple)
                        print (triple)
                    
                    
                    
                    
                    
                    

                    
        
        return list(check)
