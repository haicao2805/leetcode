from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(s.minimumTotal([[-10]]))
