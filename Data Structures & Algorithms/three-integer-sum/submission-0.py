class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for index, value in enumerate(nums):
            if (index > 0) and (value == nums[index-1]):
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                currentsum = value + nums[left] + nums[right]
                if currentsum > 0:
                    right -= 1 
                elif currentsum < 0:
                    left += 1
                else: 
                    triplets.append([value, nums[left], nums[right]])
                    left += 1
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
        return triplets
