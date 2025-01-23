from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        rows, cols = [], []

        for r in range(M):
            rowSum = 0
            for c in range(N):
               rowSum += grid[r][c]

            if rowSum > 1:
                res += rowSum
                rows.append(r)

        for c in range(N):
            colSum = 0
            for r in range(M):
               colSum += grid[r][c]

            if colSum > 1:
                res += colSum
                cols.append(c)

        for r in rows:
            for c in cols:
                if grid[r][c]:
                    res -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countServers([[1,0],[0,1]]))
    print(s.countServers([[1,0],[1,1]]))
    print(s.countServers([[1,1,0,0],[0,0,1,0],[0,1,0,1],[1,1,0,1]]))
    print(s.countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))

# [1,0,0,1,0]
# [0,0,0,0,0]
# [0,0,0,1,0]
