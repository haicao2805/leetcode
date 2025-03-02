from typing import DefaultDict


class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        maxIdx = -1
        hmap = DefaultDict()
        for [id, val] in nums1:
            maxIdx = max(maxIdx, id)
            hmap[id] = val

        for [id, val] in nums2:
            maxIdx = max(maxIdx, id)
            if id in hmap:
                hmap[id] += val
            else:
                hmap[id] = val

        res = []
        for i in range(1, maxIdx + 1):
            if i in hmap:
                res.append([i, hmap[i]])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
    print(s.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))
