from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)

        bottomLeft = [[] for _ in range(N)]
        topRight = [[] for _ in range(N - 1)]

        for i in range(N):
            for j in range(i + 1):
                bottomLeft[i - j].append(grid[i][j])
            for j in range(i + 1, N):
                topRight[j - i - 1].append(grid[i][j])

        for arr in bottomLeft:
            arr.sort(reverse=True)
        for arr in topRight:
            arr.sort()

        for i in range(N):
            for j in range(i + 1):
                grid[i][j] = bottomLeft[i - j].pop(0)
            for j in range(i + 1, N):
                grid[i][j] = topRight[j - i - 1].pop(0)

        return grid


if __name__ == "__main__":
    s = Solution()
    print(s.sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]))
    print(s.sortMatrix([[0, 1], [1, 2]]))
    print(s.sortMatrix([[1]]))
