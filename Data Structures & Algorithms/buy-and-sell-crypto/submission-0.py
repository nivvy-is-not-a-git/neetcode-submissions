class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer = 0
        maximum = 0
        1, 2, 3
        while (pointer<len(prices)):
            for i in range(pointer+1, len(prices)):    #2 , 2
                if prices[i]-prices[pointer]>maximum:
                    maximum = prices[i]-prices[pointer]
            pointer+=1
        return maximum

        
            