class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen = [False] * 101
        for i in range(len(nums) - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]))
    print(s.minimumOperations([4, 5, 6, 4, 4]))
