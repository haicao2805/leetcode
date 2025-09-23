class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")

        for i in range(max(len(revisions1), len(revisions2))):
            v1 = int(revisions1[i]) if i < len(revisions1) else 0
            v2 = int(revisions2[i]) if i < len(revisions2) else 0
            print(v1, v2)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


if __name__ == "__main__":
    print(Solution().compareVersion("1.01", "1.001"))
    print(Solution().compareVersion("1.2", "1.10"))
    print(Solution().compareVersion("1.0", "1.0.0.0"))
