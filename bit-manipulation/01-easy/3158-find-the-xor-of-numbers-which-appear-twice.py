from typing import List


# Sort
class SortSolution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0

        sortedNums = sorted(nums)

        for i in range(1, len(nums)):
            if sortedNums[i] ^ sortedNums[i - 1] == 0:
                res ^= sortedNums[i]

        return res


# Hashmap
class HashmapSolution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hmap = {}
        res = 0
        for n in nums:
            if n in hmap:
                res ^= n
            hmap[n] = 1
        return res
