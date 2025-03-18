class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        res = 1
        start = 0
        trackBits = 0

        def printBit(bits: int):
            for i in range(31, -1, -1):
                print(bits >> i & 1, end="")
            print()

        printBit(trackBits)

        for end in range(len(nums)):
            while trackBits & nums[end] != 0:
                trackBits ^= nums[start]
                start += 1
            trackBits |= nums[end]
            printBit(trackBits)
            res = max(res, end - start + 1)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestNiceSubarray(nums=[1, 3, 8, 48, 10]))
