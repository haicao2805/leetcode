class Solution:
    def shortestPalindrome(self, s: str) -> str:
        lastIdx = 0
        prefix = 0
        suffix = 0
        base = 37
        m = 1_000_000_007
        power = 1

        for i, c in enumerate(s):
            num = ord(c) - ord("a") + 1
            prefix = (prefix * base + num) % m
            suffix = (suffix + power * num) % m
            power = power * base

            if prefix == suffix:
                lastIdx = i

        subStr = s[lastIdx + 1 :]
        reversedStr = subStr[::-1]

        return reversedStr + s


if __name__ == "__main__":
    s = Solution()
    print(s.shortestPalindrome("abcd"))
