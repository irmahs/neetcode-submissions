class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        temp = 0 
        result = []
        while temp!= target or (left <= right):
            temp = numbers[left] + numbers[right]
            if temp > target:
                right -= 1
            if temp < target:
                left += 1 
            if temp == target:
                result.append(left+1)
                result.append(right+1)
                break
        return result
        