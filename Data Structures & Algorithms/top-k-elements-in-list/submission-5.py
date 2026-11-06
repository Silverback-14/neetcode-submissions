class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        arr = []

        for num, count in count.items():
            arr.append([num, count])
        
        arr.sort(key = lambda x: x[1])

        res = []
        
        while k!=0:
            res.append(arr.pop()[0])
            k-=1
        
        return res

            