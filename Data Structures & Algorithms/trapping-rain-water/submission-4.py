class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        water = [0] * len(height)
        result = 0
        left_max[0] = height[0]
        for i in range(0, len(height), +1):
            left_max[i] = max(left_max[i-1], height[i])
        right_max[len(height)-1] = height[len(height)-1]
        for j in range(len(height)-2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j])
        for k in range(len(height)):
            water[k] = min(left_max[k], right_max[k]) - height[k]
        for k in water:
            result += k
        return result