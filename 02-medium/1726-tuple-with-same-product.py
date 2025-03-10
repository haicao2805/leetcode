from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hmap = {}
        N = len(nums)
        res = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] * nums[j] not in hmap:
                    hmap[nums[i] * nums[j]] = 1
                else:
                    hmap[nums[i] * nums[j]] += 1

        for v in hmap.values():
            if v >= 2:
                res += int(8 * v * (v - 1) / 2)
        return res
