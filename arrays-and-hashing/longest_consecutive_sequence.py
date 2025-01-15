class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_counter = 0
        for i in nums:
            if (i - 1) not in nums_set:
                counter = 0
                while (i + counter) in nums_set:
                    counter = counter + 1
                max_counter = max(max_counter, counter)
        return max_counter