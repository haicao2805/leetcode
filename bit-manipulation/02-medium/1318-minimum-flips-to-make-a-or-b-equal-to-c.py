class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        i = 0
        while a | b != c:
            bitA, bitB, bitC = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if bitA | bitB == bitC:
                i += 1
                continue
            if bitC == 1:
                res += 1
                a = a | (1 << i)
            else:
                res += bitA + bitB
                if bitA == 1: a = a ^ (1 << i)
                if bitB == 1: b = b ^ (1 << i)
            i += 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minFlips(2,6,5) == 3)
    print(s.minFlips(4,2,7) == 1)
    print(s.minFlips(1,2,3) == 0)
