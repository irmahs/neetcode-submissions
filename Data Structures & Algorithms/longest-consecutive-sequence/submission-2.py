class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setlist = set(nums)
        result = 0
        for i in range(len(nums)):
            possiblestart = nums[i] - 1
            if possiblestart not in setlist:
                j = 0
                nextnum = nums[i]+1
                temp = 1
                while j < len(setlist):
                    if nextnum in setlist:
                        temp += 1
                        nextnum += 1
                    if temp > result:
                        result = temp
                    j += 1
        return result