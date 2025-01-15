class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        storage = []
        for i in range(0, len(nums)):
            nums_clone = nums.copy()
            nums_clone.pop(i)
            product = 1
            for j in range(0, len(nums)-1):
                product = product * nums_clone[j]
            storage.append(product)
        return storage