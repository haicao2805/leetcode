from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain)
        alts = [0 for _ in range(N + 1)]
        res = 0
        for i in range(1, N + 1):
            alts[i] = gain[i - 1] + alts[i - 1]
            res = max(res, alts[i])

        return res
