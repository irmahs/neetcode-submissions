class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d.setdefault(n, 0)
            d[n] += 1
        output = []
        buckets = [[] for i in range(len(nums) + 1)]
        for number, count in d.items():
            buckets[count].append(number)
        for i in range(len(nums), 0, -1):
            for number in buckets[i]:
                output.append(number)
                if len(output) == k:
                    return output