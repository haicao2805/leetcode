class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(num: int):
            count = 0
            while num:
                count += num & 1
                num = num >> 1
            return count

        res = num1
        count1, count2 = count_bits(num1), count_bits(num2)

        idx = 0
        while count2 < count1:
            if res >> idx & 1 == 1:
                count1 -= 1
                res = res ^ (1 << idx)
            idx += 1
        while count2 > count1:
            if res >> idx & 1 == 0:
                count1 += 1
                res = res | (1 << idx)
            idx += 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minimizeXor(12,7))
    print(s.minimizeXor(1,12))
    print(s.minimizeXor(3,5))
    print(s.minimizeXor(25,72))


# The class below is old and bad Solution
class OldAndBadSolution:
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
