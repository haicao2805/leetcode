class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        for hor in ["E", "W"]:
            for ver in ["N", "S"]:
                kk, x, y = k, 0, 0
                for ch in s:
                    if ch == hor and kk:
                        ch = "E" if ch == "W" else "W"
                        kk -= 1
                    elif ch == ver and kk:
                        ch = "S" if ch == "N" else "N"
                        kk -= 1
                    x += 1 if ch == "E" else -1 if ch == "W" else 0
                    y += 1 if ch == "N" else -1 if ch == "S" else 0
                    res = max(res, abs(x) + abs(y))
        return res
