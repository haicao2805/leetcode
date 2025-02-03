class Solution:
    def findValidPair(self, s: str) -> str:
        hmap = {}  # digit -> freq

        for c in s:
            digit = ord(c) - ord("0")
            if digit not in hmap:
                hmap[digit] = 1
            else:
                freq = hmap.get(digit, 0)
                hmap[digit] = freq + 1

        for i in range(1, len(s)):
            digit = ord(s[i]) - ord("0")
            preDigit = ord(s[i - 1]) - ord("0")
            freq = hmap.get(digit, 0)
            prevFreq = hmap.get(preDigit, 0)
            if digit == preDigit or freq != digit or prevFreq != preDigit:
                continue
            return str(preDigit) + str(digit)
        return ""
