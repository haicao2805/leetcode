from typing import List


class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> int:
        if len(str1) > len(str2):
            return 0

        if str1 == str2:
            return 1

        prefix = str2[0 : len(str1)]
        if prefix != str1:
            return 0

        suffix = str2[-len(str1) :]
        if suffix != str1:
            return 0

        if prefix == suffix:
            return 1

        return 0

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                res += self.isPrefixAndSuffix(words[i], words[j])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
    print(s.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
