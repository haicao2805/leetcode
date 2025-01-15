class Solution:
    def countSetBits(self, num: int):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def minimizeXor(self, num1: int, num2: int) -> int:
        res = 0
        countBitsNum2 = self.countSetBits(num2)
        bits = []
        while num1 > 0:
            bits.append(num1 & 1)
            num1 >>= 1

        for i,v in enumerate(bits[::-1]):
            if v == 1 and countBitsNum2:
                countBitsNum2 -= 1
                res += pow(2, len(bits) - i - 1)

        for i,v in enumerate(bits):
            if v == 0 and countBitsNum2:
                countBitsNum2 -= 1
                res += pow(2, i)

        n = len(bits)
        while countBitsNum2:
            res += pow(2, n)
            n += 1
            countBitsNum2 -= 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minimizeXor(3,5))
    print(s.minimizeXor(1,12))
    print(s.minimizeXor(11,12))


# 1011
# 1010
# 0001

# 1000100
