class Solution:
    def formatString(self, s: str) -> str:
        return "".join(
            char.lower()
            for char in s
            if "a" <= char.lower() <= "z" or "0" <= char.lower() <= "9"
        )

    def isPalindrome(self, s: str) -> bool:
        prefix, suffix = 0, 0
        base = 37
        m = 1_000_000_007
        power = 1

        formatted = self.formatString(s)
        for char in formatted:
            prefix = (prefix * base + (ord(char) - ord("a") + 1)) % m
            suffix = (suffix + (ord(char) - ord("a") + 1) * power) % m
            power = (power * base) % m

        return prefix == suffix


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(" "))
    print(s.isPalindrome("0P"))
