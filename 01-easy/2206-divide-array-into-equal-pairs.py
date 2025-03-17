from typing import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        couter = Counter(nums)
        for v in couter.values():
            if v % 2 == 1:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.divideArray([3, 2, 3, 2, 2, 2]))
    print(s.divideArray([1, 2, 3, 4]))
