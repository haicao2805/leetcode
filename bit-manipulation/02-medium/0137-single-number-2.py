from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = {}
        res = 0
        for n in nums:
            res ^= n
            if not hmap.get(n):
                hmap[n] = 1
            elif hmap.get(n) == 1:
                res ^= n
                hmap[n] = 2
        return res
