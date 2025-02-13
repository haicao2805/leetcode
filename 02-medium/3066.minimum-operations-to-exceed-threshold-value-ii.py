from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        x = heapq.heappop(nums)
        res = 0
        while x < k:
            res += 1
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            x = heapq.heappop(nums)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2, 11, 10, 1, 3], 10))
    print(s.minOperations([1, 1, 2, 4, 9], 20))
