from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Prefix sum for the left side
        pre_sum_left = [0] * len(nums)
        pre_sum_left[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum_left[i] = nums[i] + pre_sum_left[i - 1]

        # Prefix sum for the right side
        pre_sum_right = [0] * len(nums)
        pre_sum_right[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            pre_sum_right[i] = nums[i] + pre_sum_right[i + 1]

        # Count valid splits
        res = 0
        for i in range(len(nums) - 1):
            if pre_sum_left[i] >= pre_sum_right[i + 1]:
                res += 1

        return res
