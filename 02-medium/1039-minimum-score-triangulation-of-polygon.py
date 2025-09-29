from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp: List[List[float]] = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            # i is starting vertex
            for i in range(n - length + 1):
                # j is ending vertex
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    score = values[i] * values[j] * values[k]
                    total = dp[i][k] + dp[k][j] + score
                    dp[i][j] = min(dp[i][j], total)

        return int(dp[0][n - 1])


if __name__ == "__main__":
    s = Solution()
    print(s.minScoreTriangulation([1, 2, 3]))
    print(s.minScoreTriangulation([3, 7, 4, 5]))
