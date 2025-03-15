class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        L, R = 1, max(nums)
        N = len(nums)

        def check(x: int) -> bool:
            total = 0

            idx = 0
            while idx < N:
                if nums[idx] <= x:
                    total += 1
                    idx += 2
                else:
                    idx += 1

            return total >= k

        while L <= R:
            M = L + (R - L) // 2
            if check(M):
                R = M - 1
            else:
                L = M + 1

        return L


if __name__ == "__main__":
    s = Solution()
    print(s.minCapability(nums=[2, 3, 5, 9], k=2))
    print(s.minCapability(nums=[2, 7, 9, 3, 1], k=2))
