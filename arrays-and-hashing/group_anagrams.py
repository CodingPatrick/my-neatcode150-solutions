class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for i in strs:
            sortedI = "".join(sorted(i))
            storage[sortedI].append(i)
        return list(storage.values())