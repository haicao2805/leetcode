class Solution:
    def maxDifference(self, s: str) -> int:
        oddFreq = 0
        evenFreq = len(s) + 1
        hmap = {}
        for c in s:
            if c not in hmap:
                hmap[c] = 1
            else:
                hmap[c] += 1

        for v in hmap.values():
            if v % 2 == 1:
                oddFreq = max(oddFreq, v)
            if v % 2 == 0:
                evenFreq = min(evenFreq, v)

        return oddFreq - evenFreq
