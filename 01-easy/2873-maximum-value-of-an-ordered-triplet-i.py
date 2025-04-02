class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    val = (nums[i] - nums[j]) * nums[k]
                    res = max(val, res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maximumTripletValue([12, 6, 1, 2, 7]))
