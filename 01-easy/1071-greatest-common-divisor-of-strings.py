from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        len1, len2 = len(str1), len(str2)
        return str1[: gcd(len1, len2)]


if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))
