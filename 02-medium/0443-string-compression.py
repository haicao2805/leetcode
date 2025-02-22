from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            length = 1
            while i + length < len(chars) and chars[i + length] == chars[i]:
                length += 1
            chars[res] = chars[i]
            res += 1
            if length > 1:
                strLength = str(length)
                chars[res : res + len(strLength)] = list(strLength)
                res += len(strLength)
            i += length
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
