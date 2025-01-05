from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = []
        right = []
        map_left = {}
        map_right = {}

        # Create prefix sums for the left
        left.append(nums[0])
        map_left[left[0]] = 1
        for i in range(1, len(nums)):
            left.append(nums[i] + left[i - 1])
            map_left[left[i]] = i + 1

        # Create prefix sums for the right
        right.append(nums[-1])
        map_right[right[0]] = 1
        for i in range(1, len(nums)):
            right.append(nums[-(i + 1)] + right[i - 1])
            map_right[right[i]] = i + 1

        # Find the minimum operations
        res = len(nums) + 1
        for value in left:
            l = map_left.get(value)
            if l and value == x:
                res = min(res, l)
                continue

            r = map_right.get(x - value)
            if l and r:
                res = min(res, l + r)

        for value in right:
            r = map_right.get(value)
            if r and value == x:
                res = min(res, r)
                continue

            l = map_left.get(x - value)
            if l and r:
                res = min(res, l + r)

        return res if res <= len(nums) else -1
