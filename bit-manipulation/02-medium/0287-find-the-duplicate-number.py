from typing import List

# Bit manipulation
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0

        for bit in range(32):
            x, y = 0, 0
            for i in range(len(nums)):
                x += nums[i] & (1 << bit)
                y += i & (1 << bit)

            if x > y:
                res |= 1 << bit

        return res


# Hashmap
class HashMapSolution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {}
        for n in nums:
            if n in hmap:
                return n
            hmap[n] = 1
        return -1
