from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        # First pass: populate the map
        for i in range(len(nums)):
            map[target - nums[i]] = i

        # Second pass: find the solution
        for i in range(len(nums)):
            j = map.get(nums[i])
            if j is not None and i != j:
                return [i, j]

        # Default return (if no solution exists, although problem guarantees a solution)
        return [0, 1]
