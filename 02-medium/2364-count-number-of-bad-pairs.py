from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        validPairs = 0
        hmap = {}
        tmp = [i - nums[i] for i in range(N)]
        for v in tmp:
            if v not in hmap:
                hmap[v] = 1
            else:
                hmap[v] += 1

        for v in hmap.values():
            if v > 1:
                validPairs += int(v * (v - 1) / 2)

        return int(N * (N - 1) / 2) - validPairs


if __name__ == "__main__":
    s = Solution()
    print(s.countBadPairs([4, 1, 3, 3]))
    # print(s.countBadPairs([1, 2, 3, 4, 5]))

# j - nums[j] != i - nums[i]
#  4 1  3 3
#  0 1  2 3
# -4 0 -1 0

#  1  2  3  4
#  0  1  2  3
# -1 -1 -1 -1
