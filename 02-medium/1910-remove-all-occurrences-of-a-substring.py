class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            pos = s.find(part)
            s = s[:pos] + s[pos + len(part) :]

        return s


if __name__ == "__main__":
    s = Solution()
    print(
        s.removeOccurrences(
            "daabcbaabcbc",
            "abc",
        )
    )
    print(s.removeOccurrences("axxxxyyyyb", "xy"))
