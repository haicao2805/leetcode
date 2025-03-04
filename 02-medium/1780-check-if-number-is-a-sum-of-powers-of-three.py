class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powOfThree = [0] * 16
        for i in range(16):
            powOfThree[i] = pow(3, i)

        flag = 15
        while True:
            found = False
            for i in range(flag, -1, -1):
                if powOfThree[i] <= n:
                    found = True
                    n -= powOfThree[i]
                    flag = i - 1
                    break
            if not found:
                break

        return n == 0


if __name__ == "__main__":
    s = Solution()
    print(s.checkPowersOfThree(12))
    print(s.checkPowersOfThree(91))
    print(s.checkPowersOfThree(21))
