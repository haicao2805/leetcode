class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        nums.sort()
        res, N = 0, len(nums)
        target = nums[N // 2]
        for n in nums:
            if n % x != target % x:
                return -1
            res += abs(target - n) // x
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([[9, 4], [6, 8]], 2))
