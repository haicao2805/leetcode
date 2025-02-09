class Solution:
    def getSum(self, a: int, b: int) -> int:
        def adderCircuit(x: int, y: int, c: int):
            sum = (x ^ y) ^ c
            carry = (x & y) | ((x ^ y) & c)
            return (sum, carry)

        res, carry = 0, 0
        for idx in range(32):
            (s, c) = adderCircuit(a & 1, b & 1, carry)
            carry = c
            res |= s << idx

            idx += 1
            a >>= 1
            b >>= 1

        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.getSum(2, -3))


class SumTwoPositiveIntSolution:
    def getSum(self, a: int, b: int) -> int:
        def adderCircuit(x: int, y: int, c: int):
            sum = (x ^ y) ^ c
            carry = (x & y) | ((x ^ y) & c)
            return (sum, carry)

        res, carry, idx = 0, 0, 0
        while not (a == 0 and b == 0):
            (s, c) = adderCircuit(a & 1, b & 1, carry)
            carry = c
            res |= s << idx

            idx += 1
            a >>= 1
            b >>= 1

        if carry:
            res |= 1 << idx

        return res
