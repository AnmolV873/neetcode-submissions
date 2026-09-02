class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        num = []
        for key , value in count.items():
            num.append([value, key])
        num.sort()

        res = []
        while len(res) < k:
            res.append(num.pop()[1])
        return res

