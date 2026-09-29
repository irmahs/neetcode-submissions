class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        i = 0
        j = len(nums)-1
        prefix = 1
        suffix = 1
        output = []
        while i < len(nums):
            left.append(prefix)
            prefix = prefix * nums[i]
            i += 1
        while j >= 0:
            right.append(suffix)
            suffix = suffix * nums[j]
            j -= 1
        right.reverse()
        l = 0
        for l in range(len(nums)):
            output.append(left[l]*right[l])
            l += 1
        return output