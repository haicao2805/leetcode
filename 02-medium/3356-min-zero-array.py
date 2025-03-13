class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        N = len(nums)
        L, R = 0, len(queries)

        def canTransfrom(k) -> bool:
            s = 0
            diff = [0] * (N + 1)

            for i in range(k):
                [start, end, val] = queries[i]
                diff[start] += val
                diff[end + 1] -= val
            for i in range(N):
                s += diff[i]
                if s < nums[i]:
                    return False
            return True

        if not canTransfrom(R):
            return -1

        while L <= R:
            M = L + (R - L) // 2
            if canTransfrom(M):
                R = M - 1
            else:
                L = M + 1
        return L


if __name__ == "__main__":
    s = Solution()
    print(s.minZeroArray([5], [[0, 0, 5], [0, 0, 1], [0, 0, 3], [0, 0, 2]]))
    print(s.minZeroArray([0], [[0, 0, 2], [0, 0, 4], [0, 0, 4], [0, 0, 3], [0, 0, 5]]))
    # 0 5 -> 2
    print(
        s.minZeroArray(
            [2, 0, 2], [[0, 2, 1], [0, 2, 0], [0, 2, 0], [0, 2, 1], [1, 1, 3]]
        )
    )
    print(s.minZeroArray([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]))


class MLESolution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        N = len(nums)
        sumArr = [0] * N
        preSumArr = [[0 for _ in range(N)]]

        for [l, r, v] in queries:
            for j in range(l, r + 1):
                sumArr[j] += v
            preSumArr.append(sumArr.copy())

        def check(a: list[int]) -> bool:
            for i in range(N):
                if a[i] < nums[i]:
                    return False
            return True

        res = -1
        L, R = 0, len(preSumArr) - 1
        while L <= R:
            M = (L + R) // 2
            if check(preSumArr[M]):
                R = M - 1
                res = M if res == -1 else min(res, M)
            else:
                L = M + 1

        return res
