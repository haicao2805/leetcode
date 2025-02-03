from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        M, N = len(isWater), len(isWater[0])
        queue = []
        res = [[0 for _ in range(N)] for _ in range(M)]
        for r in range(M):
            for c in range(N):
                if isWater[r][c]:
                    queue.append((r, c))

        while queue:
            r, c = queue[0]
            queue.pop(0)
            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbors:
                if 0 <= nr < M and 0 <= nc < N and isWater[nr][nc] == 0:
                    if res[nr][nc] == 0 or res[r][c] + 1 < res[nr][nc]:
                        res[nr][nc] = res[r][c] + 1
                        queue.append((nr, nc))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.highestPeak([[0, 1], [0, 0]]))
    print(s.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
    print(
        s.highestPeak(
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
            ]
        )
    )
