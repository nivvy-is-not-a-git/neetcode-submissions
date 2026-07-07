class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        pairs = []
        for num in count:
            pairs.append((count[num], num))
        
        pairs.sort(reverse=True)

        result = []

        for i in range(k):
            result.append(pairs[i][1])
        return result


        
