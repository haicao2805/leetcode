class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        numSet = set()
        for n in nums:
            if n < k:
                return -1
            elif n > k:
                numSet.add(n)

        return len(numSet)


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([5, 2, 5, 4, 5], 2))
    print(s.minOperations([2, 1, 2], 2))
    print(s.minOperations([9, 7, 5, 3], 1))


class FirstSolution:
    def minOperations(self, nums: list[int], k: int) -> int:
        minNums = min(nums)
        if minNums < k:
            return -1

        res = 0 if minNums == k else 1
        nums = sorted(nums)
        pointer = len(nums) - 2
        while nums[pointer] >= k and pointer >= 0:
            if nums[pointer] != nums[pointer + 1]:
                res += 1
            pointer -= 1

        return res
