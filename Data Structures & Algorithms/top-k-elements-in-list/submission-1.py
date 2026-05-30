class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = []
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        max = -2000
        
        for i in range(k):
            
            for number in frequency:
                if frequency[number]!=0:
                    print (number, frequency[number], max)
                    if frequency[number]>max:
                        max = frequency[number]
                        max_number = number 
                       
            frequency[max_number]=0
            max=0
            frequent.append(max_number)
            print ('appended', max_number)
        return frequent