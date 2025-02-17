class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)

        def backtrack(s: str, used: list) -> None:
            sequences.add(s)

            for i, c in enumerate(tiles):
                if not used[i]:
                    used[i] = True
                    backtrack(s + c, used)
                    used[i] = False

        backtrack("", used)

        return len(sequences) - 1


if __name__ == "__main__":
    s = Solution()
    print(s.numTilePossibilities("AAB"))
    # print(s.numTilePossibilities("A"))
    # print(s.numTilePossibilities("AAABBC"))
