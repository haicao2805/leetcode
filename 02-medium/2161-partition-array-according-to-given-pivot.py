class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        preArr, sufArr = [], []
        cnt = 0

        for n in nums:
            if n < pivot:
                preArr.append(n)
            if n > pivot:
                sufArr.append(n)
            if n == pivot:
                cnt += 1

        return preArr + [pivot] * cnt + sufArr


if __name__ == "__main__":
    s = Solution()
    print(s.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
    print(s.pivotArray([-3, 4, 3, 2], 2))
