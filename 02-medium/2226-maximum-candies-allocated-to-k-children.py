class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def canDivide(x: int) -> bool:
            return sum(c // x for c in candies) >= k

        L, R = 1, max(candies)
        while L <= R:
            M = L + (R - L) // 2
            if canDivide(M):
                L = M + 1
            else:
                R = M - 1
        return R


class PassButNotBestSolution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        L, R = 1, max(candies)

        def canDivide(x: int) -> bool:
            if x == 0:
                return False
            allocateCnt = 0
            for c in candies:
                allocateCnt += c // x

            if allocateCnt >= k:
                return True
            return False

        while L <= R:
            M = L + (R - L) // 2
            if canDivide(M):
                L = M + 1
            else:
                R = M - 1

        return R


if __name__ == "__main__":
    s = Solution()
    print(s.maximumCandies([5, 8, 6], 3))
    print(s.maximumCandies([2, 5], 11))
    print(s.maximumCandies([5, 8, 6], 4))
    print(s.maximumCandies([5, 8, 6], 5))
    print(s.maximumCandies([1, 1, 1, 1, 1], 5))

# L = 1, R = 5 => M = 3 => False
# L = 1, R = 2 => M = 1 => False
# L = 1, R = 0 => Break
