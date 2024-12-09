class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            nums_clone = nums.copy()
            nums_clone.remove(nums_clone[i])
            product = 1
            for j in range(0, len(nums_clone)):
                product = product * nums_clone[j]
            output.append(product)
        return output