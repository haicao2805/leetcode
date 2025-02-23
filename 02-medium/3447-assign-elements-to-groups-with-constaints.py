from typing import List
import math


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        res = []
        hmap = {}
        for j, e in enumerate(elements):
            if e not in hmap:
                hmap[e] = j

        def getDiviableNums(num: int) -> List[int]:
            rs = []
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    rs.append(i)
                    rs.append(num // i)

            return rs

        for g in groups:
            diviableNums = getDiviableNums(g)
            if not len(diviableNums):
                res.append(-1)
                continue

            minIdx = len(elements)
            for num in diviableNums:
                if num in hmap:
                    minIdx = min(minIdx, hmap[num])
            if minIdx != len(elements):
                res.append(minIdx)
            else:
                res.append(-1)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.assignElements([8, 4, 3, 2, 4], [4, 2]))
