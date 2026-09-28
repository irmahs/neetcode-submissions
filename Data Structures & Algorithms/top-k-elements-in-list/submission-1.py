class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d.setdefault(n, 0)
            d[n] += 1
        sortedlist = sorted(d.items(), key = getCount, reverse = True)
        output = []
        for sortedpair in sortedlist[:k]:
            output.append(sortedpair[0])
        return output
def getCount(pair):
    return pair[1]
