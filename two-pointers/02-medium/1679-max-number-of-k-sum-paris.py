from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        N = len(nums)
        sortedNums = sorted(nums)
        L, R = 0, N - 1

        while L < R:
            s = sortedNums[L] + sortedNums[R]
            if s == k:
                res += 1
                L += 1
                R -= 1
            elif s < k:
                L += 1
            else:
                R -= 1

        return res


class BruteForceSolution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        N = len(nums)
        removed = [False for _ in range(N)]

        hmap = {}
        minus = [k - nums[i] for i in range(N)]
        for i, n in enumerate(minus):
            if n not in hmap:
                hmap[n] = [i]
            else:
                hmap[n].append(i)

        res = 0
        for i, n in enumerate(nums):
            if removed[i]:
                continue
            if n in hmap:
                for j in hmap[n]:
                    if i != j and not removed[j]:
                        removed[i] = True
                        removed[j] = True
                        res += 1
                        break

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([1, 2, 3, 4], 5) == 2)
    print(s.maxOperations([3, 1, 3, 4, 3], 6) == 1)
