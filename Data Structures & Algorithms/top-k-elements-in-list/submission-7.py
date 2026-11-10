class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = []

        for item in count.items():
            freq.append(list(item))

        freq.sort(key = lambda x: x[1])

        res = []

        while k != 0:
            res.append(freq.pop()[0])
            k-=1
        
        return res
