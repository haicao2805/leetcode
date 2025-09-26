from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        if n < 3:
            return 0

        def binarySearch(l: int, r: int, v: int) -> int:
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < v:
                    l = m + 1
                else:
                    r = m - 1
            return l

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                idx = binarySearch(j + 1, n - 1, nums[i] + nums[j])
                res += idx - j - 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.triangleNumber([3, 5, 4, 7, 8, 8, 9]))
    print(s.triangleNumber([2, 2, 3, 4]))
    print(s.triangleNumber([4, 2, 3, 4]))


class TLESolution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        def isTriangle(x: int, y: int, z: int) -> bool:
            if x + y <= z or x + z <= y or y + z <= x:
                return False
            return True

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if isTriangle(nums[i], nums[j], nums[k]):
                        res += 1

        return res
