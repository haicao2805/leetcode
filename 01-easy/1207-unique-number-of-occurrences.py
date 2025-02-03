from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}
        occurSet = set()
        for n in arr:
            if n not in hmap:
                hmap[n] = 1
            else:
                hmap[n] += 1

        for v in hmap.values():
            if v in occurSet:
                return False
            occurSet.add(v)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
