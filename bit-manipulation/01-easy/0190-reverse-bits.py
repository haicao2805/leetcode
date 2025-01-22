class Solution:
    def reverseBits(self, n: int) -> int:
        res, idx = 0, 0
        while n:
            res += pow(2, 31 - idx) if n & 1 else 0
            idx += 1
            n >>= 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(43261596))
