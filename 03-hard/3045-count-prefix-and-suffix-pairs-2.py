from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        base = 37
        m = 1_000_000_007
        hmap = {}
        res = 0

        for w in words:
            prefix = 0
            suffix = 0
            power = 1

            for i in range(len(w)):
                prefix = (prefix * base + (ord(w[i]) - ord("a") + 1)) % m
                suffix = (suffix + power * (ord(w[len(w) - i - 1]) - ord("a") + 1)) % m
                power = (power * base) % m

                if prefix == suffix:
                    res += hmap.get(suffix, 0)

            hmap[suffix] = hmap.get(suffix, 0) + 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.countPrefixSuffixPairs(
            ["bba", "aacbc", "bbba", "cabb", "aa", "aaccc", "aa", "bba", "c"]
        )
    )
    print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
    print(s.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
    print(s.countPrefixSuffixPairs(["abab", "ab"]))
    print(s.countPrefixSuffixPairs(["b", "a", "b", "a", "b"]))
    print(
        s.countPrefixSuffixPairs(
            [
                "c",
                "ccbac",
                "bc",
                "cc",
                "ba",
                "acbbc",
                "aacbc",
                "ccbbb",
                "bca",
                "bcbbb",
                "abbaa",
                "bbaa",
                "bbb",
            ]
        )
    )
