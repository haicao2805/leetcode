from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visit = [[0 for _ in range(N)] for _ in range(M)]
        res = 0

        def dfs(cell: tuple[int, int]):
            cellStack = []
            cellStack.append((cell))
            fish = 0
            while cellStack:
                r, c = cellStack.pop()
                if grid[r][c] == 0 or visit[r][c]:
                    continue

                visit[r][c] = 1
                fish += grid[r][c]

                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in neighbors:
                    if (
                        0 <= nr <= M - 1
                        and 0 <= nc <= N - 1
                        and grid[nr][nc] != 0
                        and not visit[nr][nc]
                    ):
                        cellStack.append((nr, nc))

            return fish

        for r in range(M):
            for c in range(N):
                if grid[r][c] != 0:
                    res = max(res, dfs((r, c)))

        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]) == 7)
    # print(s.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]) == 1)
    print(s.findMaxFish([[8, 6], [2, 6]]) == 22)
