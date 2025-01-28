class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        res = ""
        minLength = min(len1, len2)
        for i in range(minLength):
            res += word1[i] + word2[i]

        if len1 != len2:
            diff = abs(len1 - len2)
            res += word1[-diff:] if len1 > len2 else word2[-diff:]

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("ab", "pqrs"))
    print(s.mergeAlternately("cdf", "a"))
