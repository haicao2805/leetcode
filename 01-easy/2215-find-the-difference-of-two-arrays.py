from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        N = len(nums1)
        M = len(nums2)
        num1Set, num2Set = set(), set()

        for i in range(N):
            num1Set.add(nums1[i])
        for i in range(M):
            num2Set.add(nums2[i])

        ans1, ans2 = [], []

        for n in nums1:
            if n not in num2Set and n not in ans1:
                ans1.append(n)
        for n in nums2:
            if n not in num1Set and n not in ans2:
                ans2.append(n)

        return [ans1, ans2]
