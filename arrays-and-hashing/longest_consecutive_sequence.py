class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = list(set(nums))
        max_count = 0
        for i in nums:
            if (i - 1) not in num_set:
                count = 0
                while (i + count) in num_set:
                    count = count + 1
                max_count = max(max_count, count)
        return max_count