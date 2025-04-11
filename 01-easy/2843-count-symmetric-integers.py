class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for n in range(low, high + 1):
            if n < 100 and n % 11 == 0:
                res += 1
            elif 1000 < n < 10000:
                right = n % 10 + n % 100 // 10
                left = n // 1000 % 100 + n % 1000 // 100
                if right == left:
                    res += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countSymmetricIntegers(low=1, high=100))
    print(s.countSymmetricIntegers(low=1200, high=1230))


class ShorterSolution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(x: int) -> bool:
            s = str(x)
            if len(s) % 2 != 0:
                return False
            half = len(s) // 2
            leftSum = sum(int(c) for c in s[:half])
            rightSum = sum(int(c) for c in s[half:])
            return leftSum == rightSum

        return sum(1 for n in range(low, high + 1) if isSymmetric(n))


class FirstSolution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(x: int) -> bool:
            digits = []
            while x > 0:
                digit = x % 10
                digits.append(digit)
                x //= 10
            if len(digits) & 1 == 1:
                return False
            l, r = 0, 0
            for i, d in enumerate(digits):
                if i < len(digits) // 2:
                    l += d
                else:
                    r += d
            return l == r

        res = 0
        for n in range(low, high + 1):
            res += 1 if isSymmetric(n) else 0
        return res
