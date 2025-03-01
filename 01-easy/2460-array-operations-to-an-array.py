class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        res = []
        for n in nums:
            if n != 0:
                res.append(n)

        for i in range(N - len(res)):
            res.append(0)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.applyOperations([1, 2, 2, 1, 1, 0]))
    print(s.applyOperations([0, 1]))
