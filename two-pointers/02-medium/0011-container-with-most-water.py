from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        L, R = 0, N - 1

        res = 0
        while L < R:
            res = max(res, min(height[L], height[R]) * (R - L))

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    # print(s.maxArea([1,1]) == 1)
    print(s.maxArea([8, 7, 2, 1]) == 7)
