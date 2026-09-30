class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setlist = set(nums)
        result = 0
        for num in setlist:
            if num - 1 not in setlist:
                nextnum = num + 1
                temp = 1
                while nextnum in setlist:
                    temp += 1
                    nextnum += 1
                result = max(result, temp)
        return result