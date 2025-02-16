from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <= 1:
            return True

        cnt = 0
        for index in range(1, N):
            if nums[index] < nums[index - 1]:
                cnt += 1
        if nums[0] < nums[N - 1]:
            cnt += 1

        return cnt <= 1


if __name__ == "__main__":
    s = Solution()
    print(s.check([3, 4, 5, 1, 2]))
    print(s.check([1, 2, 3]))
    print(s.check([2, 1, 3, 4]))
