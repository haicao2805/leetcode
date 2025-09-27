from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def s(a: List[int], b: List[int], c: List[int]) -> float:
            return 0.5 * abs(
                (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
            )

        res = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    res = max(res, s(points[i], points[j], points[k]))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
    print(s.largestTriangleArea([[1, 0], [0, 0], [0, 1]]))
