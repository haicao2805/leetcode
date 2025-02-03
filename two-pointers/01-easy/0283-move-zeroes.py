from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIdx = 0
        N = len(nums)
        for i in range(N):
            if nums[i] != 0:
                nums[lastNonZeroIdx] = nums[i]
                lastNonZeroIdx += 1
        for i in range(lastNonZeroIdx, N):
            nums[i] = 0


if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))
    print(s.moveZeroes([0, 0, 0, 3, 0]))
    print(s.moveZeroes([0]))
