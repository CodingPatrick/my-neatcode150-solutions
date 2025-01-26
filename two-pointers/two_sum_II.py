class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1, r+1]
            elif summ < target:
                l = l + 1
            else:
                r = r - 1
        return []