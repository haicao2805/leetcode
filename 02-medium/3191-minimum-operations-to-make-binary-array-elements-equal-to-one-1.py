class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                res += 1
        return res if nums[len(nums) - 1] & nums[len(nums) - 2] else -1


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([0, 1, 1, 1, 0, 0]))
    print(s.minOperations([0, 1, 1, 1]))
