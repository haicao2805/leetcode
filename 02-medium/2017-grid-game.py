from typing import List
import sys


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        tmp = [[0 for _ in range(n)] for _ in range(2)]

        grid[0][0] = 0
        grid[1][n - 1] = 0

        tmp[0][0] = grid[0][0]
        tmp[1][0] = grid[1][0]
        for i in range(1, n):
            tmp[0][i] = tmp[0][i - 1] + grid[0][i]
            tmp[1][i] = tmp[1][i - 1] + grid[1][i]

        res = sys.maxsize
        for i in range(n):
            res = min(
                res, max(tmp[0][n - 1] - tmp[0][i], tmp[1][i - 1] if i > 0 else 0)
            )

        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.gridGame(
            [
                [20, 3, 20, 17, 2, 12, 15, 17, 4, 15],
                [20, 10, 13, 14, 15, 5, 2, 3, 14, 3],
            ]
        )
    )
    print(s.gridGame([[2, 5, 4], [1, 5, 1]]))
    print(s.gridGame([[3, 3, 1], [8, 5, 2]]))
    print(s.gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]))
