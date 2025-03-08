class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        preSum = [0] * N
        preSum[0] = 1 if blocks[0] == "W" else 0
        for i in range(1, N):
            preSum[i] = preSum[i - 1] + (1 if blocks[i] == "W" else 0)

        res = preSum[k - 1]
        for i in range(k, N):
            res = min(res, preSum[i] - preSum[i - k])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minimumRecolors("WBBWWBBWBW", 7))
    # 0110011010
    # 1112333445
    print(s.minimumRecolors("WBWBBW", 2))
