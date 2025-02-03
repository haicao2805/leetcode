from collections import deque
from typing import DefaultDict, List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def isValid(r: int, c: int) -> bool:
            return 0 <= r <= N - 1 and 0 <= c <= N - 1

        def bfs(r: int, c: int, label: int) -> int:
            s = 0
            q = deque([(r, c, label)])
            while q:
                r, c, label = q.popleft()
                if grid[r][c] != 1:
                    continue

                grid[r][c] = label
                s += 1

                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in neighbors:
                    if isValid(nr, nc) and grid[nr][nc] == 1:
                        q.append((nr, nc, label))
            return s

        size = DefaultDict(int)
        label = 2
        res = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = bfs(r, c, label)
                    res = max(res, size[label])
                    label += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    tmp = 1
                    hmap = {}
                    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                    for nr, nc in neighbors:
                        if isValid(nr, nc) and grid[nr][nc] != 0:
                            if grid[nr][nc] not in hmap:
                                tmp += size[grid[nr][nc]]
                                hmap[grid[nr][nc]] = 1
                    res = max(res, tmp)

        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.largestIsland([[1,0],[0,1]]))
    # print(s.largestIsland([[1,1],[1,0]]))
    print(s.largestIsland([[1, 1], [1, 1]]))
    print(
        s.largestIsland(
            [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        )
    )
