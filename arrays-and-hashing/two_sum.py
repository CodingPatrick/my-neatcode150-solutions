class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i, num in enumerate(nums):
            storage[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in storage and storage[diff] != i:
                return [i, storage[diff]]
        return []