class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                idx = 0
                while idx < len(needle) and haystack[i + idx] == needle[idx]:
                    idx += 1

                if idx == len(needle):
                    return i

        return -1
