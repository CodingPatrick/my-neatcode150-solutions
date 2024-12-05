class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            h[num] = i
        for i, num in enumerate(nums):
            if target - num in h and h[target - num] != i :
                return [i, h[target-num]]