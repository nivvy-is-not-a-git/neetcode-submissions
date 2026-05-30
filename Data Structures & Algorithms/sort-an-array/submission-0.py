class Solution:
    def merge(self, first, second):
        result = []
        i=0
        j=0
        while i<len(first) and j<len(second):
            
            if first[i]<=second[j]:
                result.append(first[i])
                i+=1
            elif second[j]<first[i]:
                result.append(second[j])
                j+=1
        result.extend(first[i:])
        result.extend(second[j:])
        print (result)
        return result
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums) //2
        first=self.sortArray(nums[:mid])
        second = self.sortArray(nums[mid:])
        if min(first)>max(second):
            return(self.merge(second, first))
        else:
            return(self.merge(first, second))

        