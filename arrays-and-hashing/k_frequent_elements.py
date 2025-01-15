class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}
        for num in nums:
            if num in storage:
                storage[num] = storage[num] + 1
            else:
                storage[num] = 1
        arr = []
        for _ in range(k):
            big = max(storage, key=storage.get)
            arr.append(big)
            storage.pop(big)
        return arr